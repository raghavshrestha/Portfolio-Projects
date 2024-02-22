
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

Q. <b>  </b><br>
```
```

Q. <b>  </b><br>
```
```

Q. <b>  </b><br>
```
```

Q. <b>  </b><br>
```
```

Q. <b>  </b><br>
```
```

Q. <b>  </b><br>
```
```
