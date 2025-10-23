# Barber Shop Data Analysis — Revenue & Customer Insights

## Project Overview
This project applies data analysis and visualisation techniques to real barber shop data to uncover actionable business insights. The goal is to understand customer behaviour, identify peak revenue periods, analyse performance across locations, and explore how data can support smarter business decisions.

I used Python & SQL to clean, explore, and visualise the data, focusing on questions such as:

- Which **days of the week** generate the most revenue? 
- What **times of day** are the most profitable?
- How does performance vary **across different locations**?
- What are the **average earnings per cut, per hour, per day and per month**?
- Are there **patterns or trends** that can help improve decision-making?


---

## Potential Insights
From the results of this project, the business owner and individual barbers could:

- **Optimise staffing and scheduling** based on peak hours
- **Adjust opening times** to maximise revenue
- **Identify low-performing days** and target them with promotions
- **Identify high-performing days** and put on extra staff to ensure efficiency
- **Forecast expected daily and monthly earnings**
- **Compare performance between locations**

---

## Data & Cleaning
The dataset contains the columns:

- Day
- Time
- Service(s)
- Money
- Tip
- Take Home
- Location
- Date
- Day of the Week

After loading in the dataset, I:

- Standardised the 'Date' and 'Time' columns
- Created new features such as 'MonthPeriod', 'Hour' and' 'Month'

Overall, the cleaning needed was very minimal since the dataset is not very large and since I created it, I ensured there were no missing entries or mistakes within the dataset when making it.


## Exploratory Data Analysis (EDA)
I explored patterns using:

- Summary statistics
- Grouped aggregations (daily, hourly, and by location)
- Visualisations (bar plots, heatmaps, line plots)

Key visual outputs included:

- **Revenue by day of week**
- **Heatmap of revenue by hour vs day**
- **Location performance comparison**
- **Revenue by period of month**
- **Average hourly rate by month**

## Tools
- **Python**(using Spyder): pandas, numpy, matplotlib, seaborn
- **SQL**

## Results
<img width="503" height="341" alt="Figure 1" src="https://github.com/user-attachments/assets/209052dc-82d0-4f46-8721-a8deb9c3f58e" />
Figure 1

<img width="503" height="341" alt="Figure 2" src="https://github.com/user-attachments/assets/5fb41961-d66a-40e8-b845-8dddea8e5f35" />
Figure 2

By taking a look at Figure 1 and Figure 2, I can compare and analyse the differences in daily average revenue between the two separate locations. It is clear that Thursdays are the quiet day in both locations, seemingly significantly so in the Marchmont branch. However, this can be explained, as I have only worked one Thursday in Marchmont which was a half-day, albeit a very quiet half-day, but this has skewed the data. Thursday in Tollcross is also the quietest day, although by significantly less of a margin. This can be taken into account however, as I tend to opt to take Thursdays off from work seeing as it is quieter than the rest of the week. 

I feel as though this can be explained by thinking about customers' thought processes. Thursday is almost the end of the week, while not quite being the weekend. Haircuts are thought in two separate ways. Firstly they can be thought of as either a chore that is taken care of when all the other chores are taken care of, like shopping or going to the post office, which tends to be earlier in the week, such as Monday or Tuesday, to get such things out of the way. Secondly, haircuts can be thought of as a treat, especially for special occasions, which often tend to take place on the weekends. This means Fridays and Saturdays tend to be the busiest days. Therefore, Thursdays are caught in between since they are neither a chore day, or a treat day, and the shops are less busy because of this.

If we compare between the two Figures we can see the daily average in Marchmont is higher, besides the two outliers Monday and Thursday(which are outliers because I have almost exclusively worked half-days on these two days in the Marchmont shop). Therefore the Marchmont shop can be declared the busier location. However, the Tollcross location is definitely more consistent.



<img width="650" height="394" alt="Figure 3" src="https://github.com/user-attachments/assets/98dec50d-2573-4107-981c-87e0a5395ae5" />
Figure 3

<img width="650" height="394" alt="Figure 4" src="https://github.com/user-attachments/assets/9c69adde-6605-4503-a0b4-c867c6c18c91" />
Figure 4

Now taking a look at Figures 3 and 4 we can see the average hourly rate for each day in each location. There are some clearly quieter and busier hours of the day from looking straight away. Mondays in Marchmont seem to be fairly quiet in the period from 12pm - 3pm so in future I would probably take that time away from the shop floor and focus on other tasks. Similarly from looking at Figure 4 it is clear that the hour 9am - 10am is fairly quiet every day in Tollcross, besides Saturdays, and 9am - 12pm everyday is certainly quieter than the afternoons. With that in mind I could take time off in the mornings to get extra rest, or I could use that time for other tasks.

We can also see the busier periods, which I want to maximise my energy and mindset for, such as Tollcross on Fridays from 11am - 3pm and Saturdays from 2pm - 5pm, and Marchmont on Wednesdays from 10am - 4pm, Fridays from 9am - 5pm, and Saturdays from 9am - 4pm. During these periods I will make sure that I have no other tasks to focus on and that the shop floor gets my full attention, ideally having my lunch break before or after these periods, and having no other tasks to focus on. 

Other interesting trends that we can take a look at are that between 10am - 11am and 12pm - 1pm in Marchmont tend to be busy everyday, with the exception of Mondays, so therefore I would want to ensure that these periods I would always be available. In Tollcross we can see the same trend for the hours 12pm - 1pm and 2pm - 3pm. It makes sense that 12pm - 1pm would bu busy because many of my customers will come for their haircuts during their lunch break from work, however I would find it difficult to explain the busy periods between 10am - 11am and 2pm - 3pm. It is also clear that the hours from 3pm - 5pm in both shops are slightly busier, which I would put down to school children finishing around that time and coming straight from school to the shop. 



<img width="612" height="394" alt="Figure 5" src="https://github.com/user-attachments/assets/a9398262-90cc-4c91-bc23-ed59d0838580" />
Figure 5

Figure 5 shows the difference in the average daily rate for each rouhgly week-long period within the month. This is the first figure that is not split between each location. This is due to not having enough data from each shop for each day in every different period, and it is also less important to see the difference in locations throughout the month and rather to see the general behaviour of customers throughout the month. 

It is clear to see that for almost every weekday (Monday - Thursday, with Friday and Saturday considered the weekend in barbering terms) the second week of the month is the peak, with the first week being not too far behind and then the third and fourth week decreasing in terms of money. This tends to be because customers view haircuts as being a bit of a bigger expense and so will wait until they have been paid to get their haircuts, so the third and fourth weeks of the month are quieter while customers have less money to spend. This is clear to see when looking at the Friday and Saturday in the "24-end" period, meaning the 24th of the month to the end of the month, as the payday for majority of customers falls on the final Thursday/Friday of the month, so the final weekend of the month is often significantly busier than any other day.

There are two outliers to the trend: the first Monday of the month is busier than every other Monday, whereas for every other day usually the second week of the month is a bit busier, and the second Friday of the month being by far the busiest day, since I would expect the final Friday of the month to be busier. The first Monday of the month can be grouped in with the busy Friday and Saturday at the end of the month, since some people will often avoid the weekend days as they are very busy, and instead come in on the next available weekday, which clearly tends to be Monday in this case at the beginning of the month.



<img width="506" height="341" alt="Figure 6" src="https://github.com/user-attachments/assets/ad9670b5-ea9c-44a7-bfcc-cc94576a9977" />
Figure 6

In Figure 6 we can see the average hourly rate by month. By doing this analysis I was able to optimise my working hours after collecting the data in June and July, and could figure out the times and days that I should be working and focusing more. This shows in the increase in rate in August and September. These months do tend to be busier than some other months because August has events like the Edinburgh Fringe Festival and schools go back so barbershops do tend to be a bit busier, and September has the universities going back so the city has a bit of a boom of students. This shows why October has a lower rate than August and Septmerb. I have optimised my working hours better because October would usually tend to be a quieter month than June and July, but it is not steadily increasing from August and September because those months are slight outliers for the year.



<img width="389" height="279" alt="Figure 7" src="https://github.com/user-attachments/assets/53a02f37-6495-4ee5-b5d4-88f1cea81d6a" />
Figure 7 

By looking at Figure 7 we can see the trend lines for the daily rate over the course of June 2025 to October 2025. This displays the 2 locations side by side and how they have performed separately as time went on. The Marchmont shop shows a gradual improvement until around mid August, where it then decreased slightly until mid September, and then increased again into mid October. This shows the higher footfall during the Fringe festival and as students started moving back, then the drop off as tourists left the city in September time, and then the gradual improvement into October as new customers from August/September came back again.

The Tollcross shop shows a steady sort of decrease and increase and then a level out into October. The initial decrease was in the quieter June and July when the city was quieter with tourists and students, and locals being on holiday. The increase in August then into September shows the busier period clearly, being closer to the city centre than Marchmont, therefore getting more of the tourist footfall and return of students. It has now decrased slightly and levelled out to the initial daily rate in June, with there being less people out and about in the centre of the city.



<img width="653" height="394" alt="Figure 8" src="https://github.com/user-attachments/assets/7c483af7-f1ec-4333-8762-ff87d56d0312" />
Figure 8

<img width="644" height="394" alt="Figure 9" src="https://github.com/user-attachments/assets/cf57a04e-c2d5-4bea-b1bf-81e6131099b5" />
Figure 9

In the final two Figures, 8 and 9, we can see the number of empty hours by day and location. There is a stark difference between the Marchmont shop and Tollcross shop, with the Tollcross shop having many more empty hours than Marchmont. I think this shows that Tollcross has customers coming in back to back and all at once
rather than a steady flow throughout the day. This leads to more intensely busy periods in Tollcross and then heavy down periods where there are hours of not doing any haircuts. This can lead to having a good few hours free to focus on other things rather than an hour here and there, but it can lead to tiredness and a lack of focus when the busy period rolls around. 
It would be good to try and advertise free space during these periods to keep the flow of customers coming, rather than having down periods and up periods.

We can link this to Figures 3 and 4 where it is clear the the empty hours and the lower hourly rates are directly correlated. For example, it is highly likely that the hours from 9am - 11am on Wednesdays in Tollcross will be empty or quiet at least so on Wednesdays I will look to spend my mornings doing other tasks or getting extra rest. Saturdays in Marchmont tend to be quieter in the late afternoon and therefore me or a colleague can leave slightly early to get on with the weekend.

## Conclusions
The analysis done here highlights a lot of useful patterns in revenue and customer behaviour which I can use to optimise business decisions, sort my work around and make plans for my life outside of the barbershop as well. In future I would really like to have a lot more data recorded which would allow me to:

- Predict future revenue
- Predict daily outcomes per month and location

I'd also like to start recording data concerning customer retention and new footfall. This would allow me to look at the times of year that new customers are coming in, and when existing customers are potentially stopping from coming, or when the new customers begin to come back for the second and third times. This would also allow me to test difference in pricing and certain discounts and such.
