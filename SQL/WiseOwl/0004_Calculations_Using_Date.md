
Source @WiseOwl (https://www.wiseowl.co.uk/sql/exercises/standard/calculations-using-dates/)<br>

## Calculations Using Dates

Q. <b> Combine the YEAR, CONVERT, and FORMAT functions to show events in your year of birth.</b>
First create a query showing events which took place in your year of birth.<br>
Amend your query so that it shows event date neatly formatted.
* Once using the FORMAT function.
* Once using the CONVERT function.
```
select 
	eventName, eventDate,
	format(eventDate,'dd/MM/yyyy') AS [UsingFormat],
	convert(varchar,eventDate,103) AS [UsingConvert]
	from tblEvent
	where Year(eventDate) = 1978
```

Q. <b> Use the DATEDIFF and the ABS functions to list the events in order of closeness to when you were born. </b>
The idea behind this exercise is to see what was happening in the world around the time when you were born(can pick any year). First Create a query to show the number of days have elapsed for any event since your birthday.(imaginary DOB: 4 March 1964)

```
select 
	eventName, format(EventDate,'dd MMM yyyy') AS [EventDate],
	DateDiff(day,'04-03-1964',eventDate) AS [DaysOffset],
	ABS(DateDiff(day,'04-03-1964',eventDate)) AS [Days difference]
	from tblEvent
	order by ABS(DateDiff(day,'04-03-1964',eventDate)) asc;
```

Q. <b>Use the DATENAME and DATEPART functions to show events taking place on Friday 13th of any month/year. </b>
Create a query to show the day of the week and also the day number on which each event occurred.<br>
Use this to show:
* That mercifully there weren't any events on Friday the 13th;
* That there was one event on Thursday the 12th (the day before); and
* That there were two events on Saturday the 14th (the day after).

```
select 
	eventName, eventDate,
	datename(weekday,eventdate) as [Day of week],
	DATEPART(day, EventDate) as [DayNumber]
	from tblEvent
	where DATENAME(weekday, EventDate) = 'Friday' 
	AND 
	DATEPART(day, EventDate) = 13 OR
	DATEPART(day, EventDate) = 13-1 OR
	DATEPART(day, EventDate) = 13+1;
```

Q. <b>Display full dates, including the correct suffix  </b>
Create a query to show full dates for any event.

```
SELECT 
	eventName,
    CONCAT(
	format(eventDate,'dddd'),' ',
        CAST(DATEPART(day, EventDate) AS VARCHAR),
        CASE 
            WHEN DATEPART(day, EventDate) IN (1, 21, 31) THEN 'st'
            WHEN DATEPART(day, EventDate) IN (2, 22) THEN 'nd'
            WHEN DATEPART(day, EventDate) IN (3, 23) THEN 'rd'
            ELSE 'th'
        END,
        ' ',
        DATENAME(month, EventDate),
        ' ',
        CAST(DATEPART(year, EventDate) AS VARCHAR)
    ) AS FullDate
FROM tblEvent
order by eventDate;
```

<i>**** Module Completed ****</i>
