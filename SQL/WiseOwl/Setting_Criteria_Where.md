
Source: @WiseOwl Training (https://www.wiseowl.co.uk/sql/exercises/standard/setting-criteria-using-where/)

## SQL exercises on SETTING CRITERIA USING WHERE CLAUSE
Q.Write a query to list out all of the events from the tblEvent table in Category number 11 (which corresponds to Love and Relationships, as it happens).<br>

```
select
  eventName, eventDate
  from tblEvent
  where CategoryId=11;
```


Q. Create a query which lists out all of the tblEvents which include the word Teletubbies.<br> 
Now add an OR condition to your query so that it lists out all events whose:<br>
  Name includes Teletubbies; or<br>
  Name includes Pandy.

```
select
  eventname,eventdate
  from tblevent where eventName LIKE('%Teletubbies%');
OR
select
  eventname,eventdate
  from tblevent
  where eventName LIKE ('%Teletubbies%') OR eventName LIKE('%Pandy%');
```


Q. <b>Use a WHERE clause to show all of the events between two given dates.</b><br>
Create a query which lists out all of the events which took place in February 2005.<br>

```
select
	eventname as [What],
	eventdate as [When]
	from tblevent
	where EventDate between '2005-02-01' AND '2005-02-28';
```


Q. 3 Challenging queries combining criteria to find possible data anomalies.<br>
Query to show	
 * Events which aren't in the Transport category (number 14), but which nevertheless 
   include the text Train in the EventDetails column. -> Returns	4 rows <br>
 
```
select top 4
	eventname as [WHAT]
	from tblevent
	where CategoryID !=14 AND EventDetails like('%train%');
```
 * Events which are in the Space country (number 13), but which don't mention Space in 
   either the event name or the event details columns.	 -> Returns 6 rows 
```
select eventName as [WHAT]
  from tblevent
  where CategoryID = 13 AND eventDetails like ('%space%');
```
<br>

 * Events which are in categories 5 or 6 (War/conflict and Death/disaster), but which 
   don't mention either War or Death in the EventDetails column. -> Returns	91 rows<br>
```
select eventname as [WHAT]
	from tblevent
	where CategoryID in(5,6) 
	AND EventDetails not like('%war%') and EventDetails not like('%death%');
```

Q. <b>Use wildcards, AND, IN and OR to get a list of events to do with water.</b><br>
First show a list of all events which might have something to do water.  The Wise Owl interpretation of this is that one or more of the following is true:
 * They take place in one of the island countries (8, 22, 30 and 35, corresponding to Japan, the Marshall Islands, 
   Cuba and Sri Lanka respectively)
 * Their EventDetails column contains the word Water (not the text Water, but the word)
 * Their category is number 4 (Natural World)
   
This should return 11 rows.  Now add a criterion to show only those events which happened since 1970 (you may need to use parentheses to get this to give the correct answer).
```
select
	eventName, eventDetails, eventDate
	from tblevent
	where eventDate>='1970-01-01'
	AND ( countryID in (8,22,30,35) 
	    OR eventDetails like '%water%'
	   OR CategoryID =4 )
	order by eventDate asc
```


*** Module Completed ***
