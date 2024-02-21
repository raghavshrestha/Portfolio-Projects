Source @WiseOwl (https://www.wiseowl.co.uk/sql/exercises/standard/calculations/4109/)<br>

## Calculations

Q. <b>List for each event the number of characters in its name.</b><br>
Create a query listing out each event with the length of its name, with the shortest event first.
<br>
```
select 
	eventName, len(eventName) as [Length of Name]
	from tblEvent
	order by [Length of Name] asc
```

Q. <b>Cast numbers as text to allow you to concatenate them together with strings.</b><br>
Create a query to list out for each event the category number that it belongs to. <br>
Apply a WHERE criteria to show only those events in country number 1.
<br>
```
select
	eventName + ' (Category ' + cast(CategoryID as varchar) + ' )' as [Event (Category)]
	, eventDate
	from tblEvent where countryID = 1
```

Q. <b> Use IsNull, Coalesce and/or CASE WHEN to replace nulls with values</b><br>
The tblContinent table is lists out the world's continents, but there are gaps.<br>
* Add upto 3 columns to show a message where a summary is missing.

Here's what your 3 columns should use:

Column         	How to get it<br>
Using ISNULL	->   Use the IsNull function to substitute the words No summary for rows where the Summary column is 
                null.<br>
Using COALESCE ->	Do the same thing, but using the COALESCE function instead.<br>
Using CASE	->    Use a CASE WHEN statement to show different things according to whether the Summary column is null 
                or not.
<br>
```
select 
	ContinentName, Summary, 
	ISNULL(Summary,'No Summary') AS [Using IsNULL],
	Coalesce(Summary,'NO SUMMARY') AS [Using Coalesce],
	CASE
		when Summary is null then 'No Summary'
		else Summary
	end AS [Using Case]

	from tblContinent
```

Q. <b> Write a CASE WHEN expression to assign countries to different groups.<b><br>
Write a query to divide countries into the groups.
<br>
```
```

Q.
<br>
```
```

Q.
<br>
```
```

Q.
<br>
```
```
