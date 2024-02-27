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
```
```
Q. <b>Use two subqueries to list all events in neither the last 30 countries or the last 15 categories. </b><br>
```
```
