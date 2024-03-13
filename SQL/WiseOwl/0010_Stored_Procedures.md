
Source @WiseOwl<br>

<b>[Stored Procedures](https://www.wiseowl.co.uk/sql/exercises/standard/stored-procedures/)</b><br>
Q. <b>Create a stored procedure to list Dr Who episodes featuring "Matt Smith" and also episodes made in 2012. </b><br>
```
USE DoctorWho
GO
create proc spMattSmithEpisodes 
as
Begin
	SELECT        
	tD.DoctorName as [Doctor], 
	tE.SeriesNumber as [Series], 
	tE.EpisodeNumber as [Episodes], 
	tE.Title, 
	tE.EpisodeDate as [Date of Episode] 
	
	FROM tblDoctor tD
	INNER JOIN tblEpisode tE ON tD.DoctorId = tE.DoctorId
	where tD.DoctorName='Matt Smith' and 
		-- te.EpisodeDate like '2012%'
		year(te.episodeDate) = 2012
	order by te.EpisodeDate asc
end
```

Q. <b>Filter the SELECT statement, only show events occurring in August. </b><br>
```
USE WorldEvents
GO
CREATE PROC uspAugustEvents
AS
BEGIN
	SELECT
	EventID,EventName,EventDetails,EventDate
	FROM tblEvent
	WHERE
		-- MONTH(EVENTDATE) = 8
		DATEPART(MM,EVENTDATE) = 8;
END
```

Q. <b>Write a basic procedure to list countries in Asia, then make small changes to it. </b><br>
Create a stored procedure called "uspCountriesAsia" to list out all the countries with ContinentID=1, in alphabetical order.<br>
```
USE WorldEvents
GO
CREATE PROC uspCountriesSelect @CONTID AS INT = 1 -- DEFAULT SET TO ASIA CONTINENT
AS
BEGIN
 SELECT COUNTRYNAME
		FROM tblCountry
		WHERE ContinentID = @CONTID 
		ORDER BY COUNTRYNAME ASC
END
```

Q. <b>Create a stored procedure to list Dr Who episodes were written by "Steven Moffat". </b><br>
```
USE [DoctorWho]
GO
/*  Creating SP with parameters so users can extract results for any desired authors  */

CREATE PROC spAuthorEpisodes @Author VARCHAR(30)
AS
BEGIN
	SELECT TE.Title
		FROM tblAuthor TA
		INNER JOIN tblEpisode TE
			ON TA.AuthorId = TE.AuthorId
		WHERE
			TA.AuthorName LIKE '%' + @Author + '%'
		ORDER BY
			TE.EpisodeDate DESC
END
```

Q. <b>Create a stored procedure to list Dr Who episodes by frequency in two ways. </b><br>
```
USE DoctorWho
GO
CREATE PROC spSummariseEpisodes
AS
BEGIN
	SELECT 
		TOP 3 TC.CompanionName,
		COUNT(*) AS EPISODES
		FROM tblCompanion TC
		INNER JOIN tblEpisodeCompanion TEC
			ON TC.CompanionId = TEC.CompanionId
		GROUP BY TC.CompanionName
		ORDER BY EPISODES DESC
END
BEGIN
	SELECT 
		TOP 3 TE.EnemyName,
		COUNT(*) AS EPISODES
		FROM tblEnemy TE
		INNER JOIN tblEpisodeEnemy TEE
			ON TE.EnemyId = TEE.EnemyId
		GROUP BY TE.EnemyName
		ORDER BY EPISODES DESC
END
GO
```

<I> **** -- Module Completed -- ****</i>
