Source @WiseOwl (https://www.wiseowl.co.uk/sql/exercises/standard/views/)<br>
<i> *** Most of the solutions is shared in the exercise itself, not continuing ahead with solutions *** </i>

##  SQL Exercises on VIEWS

Q. <b>Use the view designer to create a view, and change it in SQL. </b><br>
Include the tables tblAuthor, tblEpisode and tblDoctor, and use the view designer to
create a view listing the episodes whose titles start with F, with the following information:
```
-- For searching title starting with letter 'F'
SELECT   
	tA.AuthorName, tD.DoctorNumber, tE.Title, tE.EpisodeDate
	FROM  tblAuthor tA 
	INNER JOIN tblEpisode tE 
		ON tA.AuthorId = tEe.AuthorId
	INNER JOIN tblDoctor tD
		ON tE.DoctorId = tDd.DoctorId
	WHERE tE.Title LIKE 'F%'
----------------------------------------
-- For searching title starting with letter 'H'
SELECT   
	tA.AuthorName, tD.DoctorNumber, tE.Title, tE.EpisodeDate
	FROM  tblAuthor tA 
	INNER JOIN tblEpisode tE 
		ON tA.AuthorId = tEe.AuthorId
	INNER JOIN tblDoctor tD
		ON tE.DoctorId = tDd.DoctorId
	WHERE tE.Title LIKE 'H%'
```

Q. <b> Create a view in the view designer, tidy up its SQL and use it to select data.</b><br>
```
```

Q. <b>Script a view in a query, then use the view designer to edit it. </b><br>
```
```

Q. <b>Write a view to combine tables, then use this as a basis for a grouping query. </b><br>
```
```

Q. <b>Use views based on views to show Doctor Who episodes with only 1 enemy and 1 companion. </b><br>
```
```
