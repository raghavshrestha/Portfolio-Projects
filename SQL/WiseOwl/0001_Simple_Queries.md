
Source @WiseOwl (https://www.wiseowl.co.uk/sql/exercises)<br>


##  Simple Queries
Q. Create a query to list out the following columns from the tblEvent table, with the most recent first.<br>
<b>``` select eventName, eventDate from tblEvent order by eventDate desc; ```</b><br>

Q. Create a query to list out the id number and name of the last 3 categories from the tblCategory table in alphabetical order.<br>
<b>
```
select Top 3 
    CategoryId, CategoryName 
    from tblCategory order by CategoryName desc;
```
</b>

Q. Write a query to show the first 5 events (in date order) from the tblEvent table in chronological order.<br>
<b> 
```
select top 5 
	eventName as What,
	eventdetails as Details
	from tblEvent order by eventDate asc;
 ```
 </b>

Q. Create a query that uses two separate SELECT statements to show the first and last 2 events in date order from the tblEvent table and also redirect the output of the query to a text, rather than to the grid.<br>
<b>
```
-- For querying last 2 records
select top 2
	eventName as What,
	eventdetails as Details
	from tblEvent order by eventDate desc;

-- For querying top 2 records
select top 2
	eventName as What,
	eventdetails as Details
	from tblEvent order by eventDate asc;
```
</b>
<i> Select the "Result to text" option from the Toolbar for redirecting output to text. </i>

<br><br><br>

<i>*** Module completed ***</i>
