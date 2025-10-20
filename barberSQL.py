#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 16:41:34 2025

@author: benharris
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

df = pd.read_csv('Downloads/Barbers.csv')

# Make sure Date is parsed
df["Date"] = pd.to_datetime(df["Date"], errors="coerce", dayfirst=True)
df["Hour"] = pd.to_datetime(df["Time"], format="%H:%M").dt.hour

# Extract day of month
df["DayOfMonth"] = df["Date"].dt.day
bins = [0, 7, 15, 23, 31]
# Create roughly week long periods within the month to analyse which periods
# are busy every month
labels = ["1–7", "8–15", "16–23", "24–end"]
df["MonthPeriod"] = pd.cut(df["DayOfMonth"], bins=bins, labels=labels, right=True)

# Extract the months from the date
df["Months"] = df["Date"].dt.month
# Create bins for each month so we can look at the months separately
bins = [5, 6, 7, 8, 9, 10]
labels = ["June", "July", "August", "September", "October"]
df["Month"] = pd.cut(df["Months"], bins=bins, labels=labels, right=True)

days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
monthperiod_order = ["1–7", "8–15", "16–23", "24–end"]
month_order = ["June", "July", "August", "September", "October"]


# Load in SQL
conn = sqlite3.connect(':memory:')
df.to_sql('barbers', conn, index=False, if_exists='replace')


# This query is written to find the average amount of money that will be made in
# a day varying on the given day and which location.
# Using the WITH statement, get the total that will be made on each day
# and then average this over the days of the week that are worked.
# This gives an idea of how much can be earned by working certain days and
# which location should be chosen to work on these days.
avg_daily_takehome_query = """
WITH daily_totals AS (
    SELECT
        [Day of the Week] AS Day,
        Date,
        Location,
        SUM([Take Home]) AS total_takehome
    FROM barbers
    GROUP BY [Day of the Week], Date, Location
)
SELECT
    Day,
    Location,
    AVG(total_takehome) AS avg_daily_takehome
FROM daily_totals
GROUP BY Day, Location
ORDER BY Location,
    CASE
        WHEN day = 'Monday' THEN 1
        WHEN day = 'Tuesday' THEN 2
        WHEN day = 'Wednesday' THEN 3
        WHEN day = 'Thursday' THEN 4
        WHEN day = 'Friday' THEN 5
        WHEN day = 'Saturday' THEN 6
        WHEN day = 'Sunday' THEN 7
    END;
"""
avg_daily_takehome = pd.read_sql(avg_daily_takehome_query, conn)

# Loop over the different locations in order to create different plots for 
# each location
for loc, df_loc in avg_daily_takehome.groupby('Location'):
    # Ensure the days are in correct chronological order rather than alphabetic
    df_loc['Day'] = pd.Categorical(df_loc['Day'], categories=days_order, ordered=True)
    
    # Create the plot
    plt.figure(figsize=(8, 5))
    sns.barplot(
        data=df_loc,
        x='Day',
        y='avg_daily_takehome',
        palette='viridis'
    )
    
    # Annotate the bars with the data atop of the bar
    for i, value in enumerate(df_loc['avg_daily_takehome']):
        plt.text(
            i, 
            value,  # position just above the bar
            f"{value:.2f}", 
            ha='center', 
            va='bottom', 
            fontsize=11, 
        )
    
    # Add labels and styling
    plt.title(f"Average Take Home per Day - {loc}", fontsize=14)
    plt.xlabel("Day", fontsize=12)
    plt.ylabel("Average Take Home (£)", fontsize=12)
    # Ensure the top of the bars aren't overlapping the title
    plt.ylim(0, df_loc['avg_daily_takehome'].max() * 1.15)
    sns.despine()
    
    plt.show()



# This query is written in a similar fashion to the previous query, although 
# this query is slightly different as it is focused on the average hourly rate
# per hour and day in each location. 
# Similarly to before, the WITH statement finds the hourly totals which can
# then be averaged and sorted into the specific hours and days.
# This analysis can help to see the specific hours on any given day in which
# more or less customers can be expected, and if certain hours can be used
# to focus on other tasks if the shop is quiet.
avg_hourly_takehome_query = """ 
WITH hourly_totals AS (
    SELECT 
        [Day of the Week] AS Day,
        Date,
        Location,
        Hour,
        MonthPeriod,
        Month,
        SUM([Take Home]) AS hourly_takehome
    FROM barbers
    GROUP BY [Day of the Week], Date, Location, Hour, MonthPeriod, Month
)
SELECT
    Day,
    Location,
    Hour,
    AVG(hourly_takehome) AS avg_hourly_takehome
FROM hourly_totals
GROUP BY Day, Location, Hour
ORDER BY 
    CASE
        WHEN Day = 'Monday' THEN 1
        WHEN Day = 'Tuesday' THEN 2
        WHEN Day = 'Wednesday' THEN 3
        WHEN Day = 'Thursday' THEN 4
        WHEN Day = 'Friday' THEN 5
        WHEN Day = 'Saturday' THEN 6
        WHEN Day = 'Sunday' THEN 7
    END,
    Location, Hour;
"""
avg_hourly_takehome = pd.read_sql(avg_hourly_takehome_query, conn)

# As previously, loop over each location
for loc, df_loc in avg_hourly_takehome.groupby('Location'):
    df_loc['Day'] = pd.Categorical(df_loc['Day'], categories=days_order, ordered=True)
    pivot_df = df_loc.pivot(index='Day', columns='Hour', values='avg_hourly_takehome')

    plt.figure(figsize=(12,6))
    # Use annotated heatmap to best analyse by day and hour
    sns.heatmap(pivot_df, cmap='YlGnBu', annot=True, fmt='.1f')
    plt.title(f'Average Take Home by Day & Hour – {loc}', fontsize=14)
    plt.ylabel('Day of Week')
    plt.xlabel('Hour of Day')
    plt.show()




# This query is written to investigate the difference in times of the month
# and how they correlate with the number of customers coming to the shop.
# As per the first query, a WITH statement is used to find the total money
# that is made in each day, which is then averaged afterwards and sorted.
# This should make it clear what periods within the month are busier and are
# maybe more worthwile to take time off or bring in more staff.
avg_period_takehome_query = """ 
WITH daily_totals AS (
    SELECT
        [Day of the Week] AS Day,
        Date,
        Location,
        MonthPeriod,
        SUM([Take Home]) AS period_takehome
    FROM barbers
    GROUP BY MonthPeriod, [Day of the Week], Date, Location
)
SELECT
    MonthPeriod,
    Day,
    AVG(period_takehome) AS avg_period_takehome
FROM daily_totals
GROUP BY MonthPeriod, Day
ORDER BY
    CASE
        WHEN MonthPeriod = "1–7" THEN 1
        WHEN MonthPeriod = "8–15" THEN 2
        WHEN MonthPeriod = "16–23" THEN 3
        WHEN MonthPeriod = "24–end" THEN 4
    END,
    CASE
        WHEN Day = 'Monday' THEN 1
        WHEN Day = 'Tuesday' THEN 2
        WHEN Day = 'Wednesday' THEN 3
        WHEN Day = 'Thursday' THEN 4
        WHEN Day = 'Friday' THEN 5
        WHEN Day = 'Saturday' THEN 6
        WHEN Day = 'Sunday' THEN 7
    END;
"""
avg_period_takehome = pd.read_sql(avg_period_takehome_query, conn)

# There is no looping over location because there is not enough data for 
# each location over each period of the month to make the analysis significant.
# There is enough data to see each period of the month for all locations 
# together, which will still give a good idea of the busier and quieter periods.
avg_period_takehome['Day'] = pd.Categorical(avg_period_takehome['Day'], categories=days_order, ordered=True)
avg_period_takehome['MonthPeriod'] = pd.Categorical(avg_period_takehome['MonthPeriod'], categories=monthperiod_order, ordered=True)

plt.figure(figsize=(10,6))
# Use barplot to see side by side the difference in month-period for each day
sns.barplot(data=avg_period_takehome, x="Day", y="avg_period_takehome", hue="MonthPeriod", palette="crest")
plt.title("Average Take Home by Day and Month Period", fontsize=14)
plt.ylabel("Average Take Home (£)")
plt.xlabel("Day of Week")
plt.legend(title="Month Period")
plt.show()




# This query is used to find the hourly average from month to month.
# The WITH statement finds the hourly total, and is then averaged and sorted
# into the separate months after.
# This should help to see the ranging over time in the average hourly rate,
# as well as which months of the year are busier or quieter.
avg_hourlyrate_per_month_query = """ 
WITH hourly_totals AS (
    SELECT 
        [Day of the Week] AS Day,
        Date,
        Location,
        Hour,
        MonthPeriod,
        Month,
        SUM([Take Home]) AS hourly_takehome
    FROM barbers
    GROUP BY [Day of the Week], Date, Location, Hour, MonthPeriod, Month
)
SELECT
    Month,
    AVG(hourly_takehome) AS avg_hourlyrate_per_month
FROM hourly_totals
GROUP BY Month
ORDER BY 
    CASE
        WHEN Month = 'June' THEN 1
        WHEN Month = 'July' THEN 2
        WHEN Month = 'August' THEN 3
        WHEN Month = 'September' THEN 4
        WHEN Month = 'October' THEN 5
    END;
"""
avg_hourlyrate_per_month = pd.read_sql(avg_hourlyrate_per_month_query, conn)
avg_hourlyrate_per_month['Month'] = pd.Categorical(avg_hourlyrate_per_month['Month'], categories=month_order, ordered=True)

plt.figure(figsize=(8, 5))
# Using a barplot should help to make clear the range in differing hourly rates.
sns.barplot(
    data=avg_hourlyrate_per_month,
    x='Month',
    y='avg_hourlyrate_per_month',
    palette='viridis'
)

# Annotate the bars
for i, value in enumerate(avg_hourlyrate_per_month['avg_hourlyrate_per_month']):
    plt.text(
        i, 
        value + 0.2,  # position just above the bar
        f"{value:.2f}", 
        ha='center', 
        va='bottom', 
        fontsize=11, 
    )

# Add labels and styling
plt.title("Average Hourly Rate per Month", fontsize=14, fontweight='bold')
plt.xlabel("Month", fontsize=12)
plt.ylabel("Average Hourly Rate (£)", fontsize=12)
plt.ylim(0, avg_hourlyrate_per_month['avg_hourlyrate_per_month'].max() + 2)
sns.despine()

plt.show()





# There is no need to write a query for this plot. The data is accessed straight
# from the original dataframe.
# This plot will take all fo the money made on each day recorded and plot each
# point. This will show a line of best fit that gives a good idea of growth 
# and decline.
# This will loop over each location, although will not create two plots for each
# because it is important to see the plots on top of each other for comparison.
for loc, data in df.groupby("Location"):
    daily_takehome = data.groupby("Date")["Take Home"].sum().reset_index()
    # Find the rolling average in order to create the line of best fit
    daily_takehome["Rolling"] = daily_takehome["Take Home"].rolling(7, min_periods=1).mean()

    # Plot the datapoints
    plt.scatter(daily_takehome["Date"], daily_takehome["Take Home"], label=loc, alpha=0.5)
    # Plot the lines of best fit
    plt.plot(daily_takehome["Date"], daily_takehome["Rolling"], label=loc)

plt.legend()
plt.title("Daily Take Home by Location")
plt.xlabel("Date")
plt.ylabel("Take Home (£)")
plt.show()






# This query is very similar to the average hourly rate query but with the 
# motivation being to see which hours are generally empty abd cab therefore
# be missed.
# The number of empty hours is counted and all of the data is sorted into the
# hour, day and separate location.
no_of_empty_hours_query = """ 
SELECT 
    [Day of the Week] AS Day,
    Location,
    Hour,
    COUNT(*) AS empty_hours
FROM barbers
WHERE [Service(s)] IS NULL
GROUP BY [Day of the Week], Location, Hour
ORDER BY 
    CASE
        WHEN [Day of the Week] = 'Monday' THEN 1
        WHEN [Day of the Week] = 'Tuesday' THEN 2
        WHEN [Day of the Week] = 'Wednesday' THEN 3
        WHEN [Day of the Week] = 'Thursday' THEN 4
        WHEN [Day of the Week] = 'Friday' THEN 5
        WHEN [Day of the Week] = 'Saturday' THEN 6
        WHEN [Day of the Week] = 'Sunday' THEN 7
    END,
    Location, Hour;
"""
no_of_empty_hours = pd.read_sql(no_of_empty_hours_query, conn)

# Loop over location
for loc, df_loc in no_of_empty_hours.groupby('Location'):
    df_loc['Day'] = pd.Categorical(df_loc['Day'], categories=days_order, ordered=True)
    pivot_df = df_loc.pivot(index='Day', columns='Hour', values='empty_hours')

    plt.figure(figsize=(12,6))
    # Create annotated heatmap to best analyse the more consistently quiet hours
    sns.heatmap(pivot_df, cmap='PuBuGn', annot=True, fmt='.1f')
    plt.title(f'Number of Empty Hours by Day & Hour – {loc}', fontsize=14)
    plt.ylabel('Day of Week')
    plt.xlabel('Hour of Day')
    plt.show()



























