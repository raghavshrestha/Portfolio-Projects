Source: @WiseOwl Training (https://www.wiseowl.co.uk/sql/exercises/standard/subqueries/)

## SQL exercises on SUBQUERIES
Q. <b>Use a subquery to show events which happened since the last one for a particular country occurred. </b><br>
```
SELECT     
	tE.EventName, tE.EventDate, tC.CountryName
	FROM tblEvent tE 
	INNER JOIN tblCountry tC ON tC.CountryID = tE.CountryID 
	where tE.EventDate > (
		select MAX(EventDate)
		from tblEvent where countryID = 21 )
	order by tE.EventDate desc;
```
Q. <b>Use subqueries to filter with aggregates. </b><br>
Write a sub-query to filter events to show only those which have an event name of longer than average length.<br>
```
select 
	 TOP 5 eventName, len(eventName) as Length_Count
	from tblEvent
	where len(eventName) > (
		select AVG(len(eventName)) as AVG_Count
		from tblEvent );
```
Q. <b>Create a correlated subquery to list out all countries having more than 8 events. </b><br>
Write a query which lists out countries which have more than 8 events, using a correlated subquery rather than HAVING. <br>
```
select 
	tC.CountryName
	from tblCountry tC
	inner join tblevent tE 
		on tE.CountryID = tC.CountryID
	group by tc.CountryName
	having count(*) > 8
```
Q. <b>Using sub queries filter the select statement. </b><br>
Write a SELECT statment to return events from 3 continents with the fewest events.
```
select 
	top(3) tc.ContinentName, te.EventName
	from tblContinent tc
	inner join tblCountry tc1 on tc.ContinentID = tc1.ContinentID
	inner join tblEvent te on tc1.CountryID = te.CountryID;
```
Now underneath write another select statement which lists events for the 3 continents with the lowest COUNT events. Put the COUNT in the ORDER BY clause, not the SELECT.
```
select 
	top(3) tc.ContinentName
	from tblContinent tc
	inner join tblCountry tc1 on tc.ContinentID = tc1.ContinentID
	inner join tblEvent te on tc1.CountryID = te.CountryID
	group by tc.ContinentName
	order by count(*) asc
```
Finally, use the second SELECT as a filter in the first SELECT's WHERE clause. To do this use ContinentName IN (Sub Query)
```
select 
	tc.ContinentName, te.EventName
	from tblContinent tc
	inner join tblCountry tc1 on tc.ContinentID = tc1.ContinentID
	inner join tblEvent te on tc1.CountryID = te.CountryID
	where tc.ContinentName in ( select distinct ContinentName from tblContinent)
```
Q. <b>Use two subqueries to list all events in neither the last 30 countries or the last 15 categories. </b><br>
Create a subquery to list out all of those events whose:<br>
* CountryID is not in the list of the last 30 country IDs in alphabetical order
```
  select
	TOP(30) te.EventName, te.EventDetails
	from tblEvent te
	left outer join tblCountry tC on te.CountryID = tC.CountryID
	where te.CountryID not in
	(select top(30) CountryID from tblCountry order by CountryName desc);
```

* Category ID is not in the list of the last 15 category IDs in alphabetical order

```
select 
	TOP(15) tE.eventName, tE.EventDetails
	from tblEvent tE
	left outer join tblCategory tC on tE.CategoryID = tC.CategoryID
	where tE.CategoryID not in
		(select top(15) CategoryID from tblCategory order by CategoryName desc)
```
<br>
To produce only 8 events combine the above query for desired output.

```
select
	TOP(30) te.EventName, te.EventDetails
	from tblEvent te
	left outer join tblCountry tC on te.CountryID = tC.CountryID
	left outer join tblCategory tCa on tE.CategoryID = tCa.CategoryID
	where te.CountryID not in
	        (select top(30) CountryID from tblCountry order by CountryName desc)
	and tE.CategoryID not in
		(select top(15) CategoryID from tblCategory order by CategoryName desc);
```

<i>**** Module Completed ****</i>
