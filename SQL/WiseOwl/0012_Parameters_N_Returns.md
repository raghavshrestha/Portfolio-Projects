Source: @Wiseowl<br>
[SQL exercises on PARAMETERS AND RETURN VALUES](https://www.wiseowl.co.uk/sql/exercises/standard/parameters-and-return-values/)

Q. <b>Get a stored procedure to list the Dr Who episodes for a given enemy. </b><br>
```
USE DoctorWho
GO
CREATE PROC spEnemyEpisodes @EnemyName AS VARCHAR(30)
AS
BEGIN
	SELECT        
		TEP.SeriesNumber, TEP.EpisodeNumber, TEP.Title
		FROM tblEnemy TE 
		INNER JOIN tblEpisodeEnemy TEE ON TE.EnemyId = TEE.EnemyId 
		INNER JOIN tblEpisode TEP ON TEE.EpisodeId = TEP.EpisodeId
		WHERE TE.EnemyName like '%' + @EnemyName + '%'
		ORDER BY TEP.SeriesNumber, TEP.EpisodeNumber
END
```

Q. <b>Create a procedure to list out the companions for a given doctor. </b><br>
```
USE DoctorWho
GO
DROP PROC IF EXISTS spCompanionForDoctor
GO
CREATE PROC spCompanionForDoctor @DocName AS VARCHAR(30) = NULL
AS
BEGIN
	SELECT        
		TC.CompanionName
		FROM tblCompanion TC
		INNER JOIN tblEpisodeCompanion TEC ON TC.CompanionId = TEC.CompanionId 
		INNER JOIN tblEpisode TE ON TEC.EpisodeId = TE.EpisodeId 
		INNER JOIN tblDoctor TD ON TE.DoctorId = TD.DoctorId
		WHERE DOCTORNAME LIKE '%' + @DocName + '%' or @DocName is null
		GROUP BY TC.COMPANIONNAME
END
```

Q. <b> Create a stored procedure to list Dr Who episodes for a series number, using a default parameter value.</b><br>
```
USE DoctorWho
GO
CREATE PROC spListEpisodes @SeriesNum AS INT = NULL
AS
BEGIN
	SELECT 
		Title
		FROM tblEpisode
		WHERE SeriesNumber = @SeriesNum OR @SeriesNum IS NULL
END
```

Q. <b>Create a stored procedure with NULLs as the default values. </b><br>
```
USE WorldEvents
GO
DROP PROC IF EXISTS uspCategoryEvents
GO
CREATE PROC uspCategoryEvents 
	(@CategoryName VARCHAR(100) = NULL,
	@After AS DATETIME = NULL,
	@CategoryID AS INT = NULL)
AS
BEGIN
SELECT       
	TC.CategoryName, TE.EventDate, TE.CategoryID
	FROM tblCategory TC
	INNER JOIN tblEvent TE ON TC.CategoryID = TE.CategoryID
	WHERE
	(TC.CategoryID = @CategoryID OR @CategoryID IS NULL) AND
	(TC.CategoryName  LIKE '%' + @CategoryName + '%' OR @CategoryName IS NULL) AND
	(TE.EventDate >= @After OR @After IS NULL)
END
```

Q. <b>	Create stored procedures with default values for the parameters. </b><br>
```
```

Q. <b> Filter in a stored procedure using a parameter.</b><br>
```
```

Q. <b>Use an output parameter to return a list variable of the most eventful continents. </b><br>
```
```

Q. <b>Use return values to bring back an INT return value from a stored procedure. </b><br>
```
```

Q. <b>Count rows and pass the information out of a procedure using output parameters. </b><br>
```
```

Q. <b>Return a continent name from one procedure, and pass the output value into another. </b><br>
```
```

Q. <b>Return from a stored proecure the name of the country with the most events and how many events there were. </b><br>
```
```
<i> **** --- Module Completed --- ****</i>
