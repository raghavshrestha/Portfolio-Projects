
Source @WiseOwl (https://www.wiseowl.co.uk/sql/exercises/standard/calculations/4109/)<br>

## SQL Exercises using BASIC JOINs

Q. <b> Create a query containing a join to list out those films whose source is NA. </b><br>
```
select
	title,s.source
	from film f join source s on 
	f.sourceid=s.sourceID
	where s.sourceID=8;
```

Q. <b> Create a query using the designer, joining 2 tables, then tidy it up and comment its SQL </b><br>
```
SELECT        
	tblCountry.CountryName AS Country,
	tblEvent.EventName AS [What happened],
	tblEvent.EventDate AS [When happened]
	FROM tblCountry 
	INNER JOIN tblEvent
	ON tblCountry.CountryID = tblEvent.CountryID
	ORDER BY [When happened]
```

Q. <b> Use an inner join to link two tables together in a query </b><br>
Add columns and filters to your query so that it shows who wrote the "special" episodes.
```
SELECT 
	tblAuthor.AuthorName,
	tblEpisode.Title, 
	tblEpisode.EpisodeType
	FROM tblAuthor
	INNER JOIN tblEpisode 
	ON tblAuthor.AuthorId = tblEpisode.AuthorId
	WHERE tblEpisode.EpisodeType LIKE '%special%';
```

Q. <b> Create an inner join in a query, then change it to an outer join to show categories having no events </b><br>
* Create a query which uses an inner join to link the categories table to the events table (they share a column/field called CategoryId).
  ```
  select 
	eventName, eventDate, CategoryName
	from tblevent e
	inner join tblCategory c
	on e.CategoryID=c.CategoryID;
  ```
* Change the inner join to an outer join, so that you show for each category its events - even when there aren't any.
  ```
  select 
	eventName, eventDate, CategoryName
	from tblevent e
	full outer join tblCategory c
	on e.CategoryID=c.CategoryID;
  ```

Q. <b> Join two tables together in SQL, using alias table names </b><br>
Create a join to list out all of the doctors who appeared in episodes made in 2010.
```
SELECT      
	tblDoctor.DoctorName, tblEpisode.Title
	FROM tblDoctor 
	INNER JOIN tblEpisode
	ON tblDoctor.DoctorId = tblEpisode.DoctorId
	WHERE YEAR(tblEpisode.EpisodeDate) = 2010;
```

Q. <b> Link the continent, country and event tables with inner joins, and then filter by fields from 2 tables. </b><br>
Create a query to link together the following 3 tables:
* tblContinent
* tblCountry
* tblEvent
```
select 
	e.EventName, e.EventDate,
	c1.CountryName,c2.ContinentName
	from tblEvent e
	full join tblCountry c1
	on e.CountryID = c1.CountryID
	full join tblContinent c2
	on c1.ContinentID = c2.ContinentID
	where c1.CountryName = 'Russia' OR c2.ContinentName='Antarctic'
```

Q. <b> Use inner joins to link four tables to show Dr Who enemies by author. </b><br>
Write a query using inner joins to show all of the authors who have written episodes featuring the Daleks.
```
SELECT        
	tblAuthor.AuthorName
	FROM tblEnemy 
	INNER JOIN tblEpisodeEnemy 
	ON tblEnemy.EnemyId = tblEpisodeEnemy.EnemyId
	INNER JOIN tblEpisode 
	ON tblEpisodeEnemy.EpisodeId = tblEpisode.EpisodeId 
	INNER JOIN tblAuthor 
	ON tblEpisode.AuthorId = tblAuthor.AuthorId
	where tblEnemy.EnemyName like ('%Daleks%');
```

Q. <b> 	Use an outer join and criterion to list out the countries which have no corresponding events. </b><br>

```SELECT       
	tblCountry.CountryName
	FROM tblCountry
	FULL OUTER JOIN tblEvent
	ON tblCountry.CountryID = tblEvent.CountryID
	where tblevent.EventID is null
```

Q. <b>Use inner joins to link lots of tables together, with a WHERE clause.  </b><br>
Create a query to list out the appearances of enemies in episodes which have length under 40 characters, where the length is defined as the sum of:<br>
* the number of characters in the author's name
* the number of characters in the episode's title
* the number of characters in the doctor's name
* the number of characters in the enemy's name.
```
SELECT        
	tblAuthor.AuthorName,
	tblEpisode.Title, 
	tblDoctor.DoctorName,
	tblEnemy.EnemyName,
	len(tblAuthor.AuthorName)+
		len(tblEpisode.Title)+
		len(tblDoctor.DoctorName)+
		len(tblEnemy.EnemyName) AS [Total Length]
	FROM  tblEpisodeEnemy
	INNER JOIN tblEnemy 
		ON tblEpisodeEnemy.EnemyId = tblEnemy.EnemyId
		CROSS JOIN  tblDoctor
		INNER JOIN tblEpisode
			ON tblDoctor.DoctorId = tblEpisode.DoctorId
		INNER JOIN tblAuthor 
			ON tblEpisode.AuthorId = tblAuthor.AuthorId
	where
		( len(tblAuthor.AuthorName)+
		len(tblEpisode.Title)+
		len(tblDoctor.DoctorName)+
		len(tblEnemy.EnemyName) ) < 40

	order by [Total Length] desc
```

<i> *** Module Completed ***</i>
