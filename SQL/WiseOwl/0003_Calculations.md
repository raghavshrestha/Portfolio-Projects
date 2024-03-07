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

Q. <b> Write a CASE WHEN expression to assign countries to different groups.</b><br>
Write a query to divide countries into the groups.
<br>
```
select 
	countryName, 
	case
		when ContinentID in (1,3) then 'Eurasia'
		when ContinentID in (5,6) then 'Americas'
		when ContinentID in (2,4) then 'Somewhere hot'
		when ContinentID =7 then 'Somewhere cold'
		else 'Somewhere else'
	end AS [Countrylocation]
	from tblCountry
	order by [Countrylocation] desc
```

Q. <b>Divide events according to whether their first/last letters are the same or vowels.</b><br>
```
select 
	eventName,
	case
		when left(eventName,1) = right(eventName,1) then 'Same Letters'
		when left(eventName,1) in('a','e','i','o','u') and
		right(eventName,1) in('a','e','i','o','u') then 'Begins and Ends with Vowels'
		else 'Mixtures'
	end AS [Verdicts]

	from tblEvent
	where
		left(eventName,1) = right(eventName,1) OR
		(
		left(eventName,1) in('a','e','i','o','u') and
		right(eventName,1) in('a','e','i','o','u') )

```

Q. <b>Use the % modulus operator and a lot of ingenuity to show how big each country is relative to Wales</b><br>

```
select
	country,Kmsquared,
	kmsquared/20761 AS [WalesUnits],
	kmsquared - kmsquared/20761*20761 AS [AreaLeftOver],
	CASE
		when kmsquared/20761 <=0 then 'Smaller than Wales'
		else CONCAT((KmSquared - (KmSquared % 20761))/20761, 
					' x Wales plus ', KmSquared % 20761, ' sq. km.')
	end  AS WalesComparison
	from countriesbyarea
	order by country asc
```

Q.<b>Use the CHARINDEX function multiple times to show the number of characters between two words in a text string.</b><br>
The aim of this exercise is to find "this" and "that" in the EventDetails using CHARINDEX() function.
```
select 
	eventName,
	CHARINDEX('this',eventDetails,1) AS [thisPosition],
	CHARINDEX('that',eventDetails,1) AS [thatPosition],
	CHARINDEX('that',eventDetails,1) - CHARINDEX('this',eventDetails,1) AS [Offset]
	from tblEvent
	where eventDetails like('%this%') AND eventDetails like ('%that%')
	AND CHARINDEX('that',eventDetails,1) > CHARINDEX('this',eventDetails,1)
```


<i>*** Module Completed ***</i>
