
Source @WiseOwl (https://www.wiseowl.co.uk/sql/exercises/standard/aggregation-and-grouping/)<br>

## SQL exercises on AGGREGATION and GROUPING

Q. <b>Use COUNT, MAX and MIN to show statistics about the rows in the events table. </b><br>
```
select 
	count (*), max(eventDate) AS [Last Date],
	min(eventDate) AS [First Date]
	from tblevent;
```

Q. <b>Use GROUP BY and COUNT to report on the number of events for each category. </b><br>
Create a query which:<br>
* groups by the category name from the category table;
```
select
	tc.CategoryName 
	from tblevent te
	inner join tblCategory tc
	on te.categoryID = tc.CategoryID
	group by tc.CategoryName;
```
* counts the number of events for each.
```
select
	tc.CategoryName ,count(*) AS [Number of Events]
	from tblevent te
	inner join tblCategory tc
	on te.categoryID = tc.CategoryID
	group by tc.CategoryName
	order by [Number of Events] desc;
```

Q. <b>Use grouping to show how many episodes each Doctor Who author wrote. </b><br>
Create a query to show for each author:<br>
* the number of episodes they wrote;
* their earliest episode date; and
* their latest episode date.
```
SELECT        
	ta.AuthorName, count(*) AS [Episodes],
	min(te.episodeDate) as [Earliest Date],
	max(te.episodeDate) as [Latest Date]
	FROM tblAuthor ta 
	INNER JOIN tblEpisode te 
	ON ta.AuthorId = te.AuthorId
	group by ta.AuthorName
	order by [Episodes] desc;
```

Q. <b>Group by 2 fields and use HAVING clause to show popular combinations </b><br>
Write a query to list out for each author and doctor the number of episodes made, but restrict your output to show only the author/doctor combinations for which more than 5 episodes have been written.
```
SELECT        
	tA.AuthorName, tD.DoctorName,
	COUNT(tE.EpisodeId) AS [Episodes]
	FROM tblAuthor tA 
	INNER JOIN tblEpisode tE 
		ON tA.AuthorId = tE.AuthorId 
	INNER JOIN tblDoctor tD 
		ON tE.DoctorId = tD.DoctorId
	group by tA.AuthorName, tD.DoctorName
	Having COUNT(tE.EpisodeId) > 5
	order by [Episodes] desc;
```

Q. <b>Use SELECT, FROM, WHERE, GROUP BY, HAVING and ORDER BY to list non-European busy countries. </b><br>
Create a query listing out for each continent and country the number of events taking place therein:
```
SELECT        
	tCon.ContinentName, tC.CountryName,
	Count(tE.eventID) AS [Number of Events]
	FROM tblContinent tCon
	INNER JOIN tblCountry tC
	ON tCon.ContinentID = tC.ContinentID
	INNER JOIN tblEvent tE
	ON tC.CountryID = tE.CountryID
	group by tCon.ContinentName, tC.CountryName
	order by tC.CountryName
```

Q. <b>Combine CAST, AVG, COUNT, LEN, UPPER and LEFT to show the average length of event names by category initial. </b><br>
Create a query which shows two statistics for each category initial:<br>
* The number of events for categories beginning with this letter; and
* The average length in characters of the event name for categories beginning with this letter.
```
select 
	left(tc.CategoryName,1) AS [Category initial],
	count(tE.eventID) AS [Number of Events],
	cast(avg(cast(len(tE.eventName) AS FLOAT)) AS decimal(5,2)) AS [Average event name length]
	from tblEvent tE
	INNER JOIN tblCategory tC 
		ON tE.CategoryID = tC.CategoryID
		group by left(tc.CategoryName,1);
```

Q. <b>Use a complex CASE statement to show the number of events for each century, including the CUBE function. </b><br>
```

select 
	CASE
		WHEN left(cast(Year(eventDate) AS VARCHAR),2) ='18' 
			THEN '18th Century'
		WHEN left(cast(Year(eventDate) AS VARCHAR),2) ='19' 
			THEN '19th Century'
		WHEN left(cast(Year(eventDate) AS VARCHAR),2) ='20' 
			THEN '20th Century'
		else '21st Century'
	END AS [Century],
	count(*) AS [Number of Events]
	from tblEvent
	group by CUBE(
	CASE
		WHEN left(cast(Year(eventDate) AS VARCHAR),2) ='18' 
			THEN '18th Century'
		WHEN left(cast(Year(eventDate) AS VARCHAR),2) ='19' 
			THEN '19th Century'
		WHEN left(cast(Year(eventDate) AS VARCHAR),2) ='20' 
			THEN '20th Century'
		else '21st Century'
	END
	)
	order by [Century];
```

Q. <b> Use lots of grouping and criteria to list out year/doctor episode counts.</b><br>
Write a query to list out for each episode year and enemy the number of episodes made, but in addition:<br>
* Only show episodes made by doctors born before 1970; and
* Omit rows where an enemy appeared in only one episode in a particular year.
```
SELECT
	year(e.EpisodeDate) as 'Episode year',
	en.EnemyName,
	COUNT(*) AS 'Number of episodes'
FROM
	tblEpisode as e
	INNER JOIN tblDoctor as d on e.DoctorId = d.DoctorId
	INNER JOIN tblEpisodeEnemy as ee ON e.EpisodeId = ee.EpisodeId
	INNER JOIN tblEnemy as en on en.EnemyId = ee.EnemyId
WHERE
	year(d.BirthDate) < 1970
GROUP BY
	year(e.EpisodeDate),
	en.EnemyName
HAVING
	COUNT(*) > 1
ORDER BY
	'Number of episodes' DESC
```

<i> **** Module Completed ****</i>
