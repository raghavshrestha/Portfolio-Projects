Source: @WiseOwl<br>
[SQL exercises on VARIABLES](https://www.wiseowl.co.uk/sql/exercises/standard/variables/)

Q. <b>Use a variable holding a row id to get at the details for a row.</b><br>
```
USE DoctorWho
GO
CREATE PROC spCountByNumbers
AS
BEGIN
	DECLARE @EpisodeID int = 54

	DECLARE @EpisodeName varchar(max) = (
		SELECT title
			from tblEpisode
			where EpisodeId = @EpisodeID )

	DECLARE @NumberCompanions int = (
		SELECT count(*)
			from tblEpisodeCompanion
			where EpisodeId = @EpisodeID )

	DECLARE @NumberEnemies int = (
		SELECT count(*)
			from tblEpisodeEnemy
			where EpisodeId = @EpisodeID )

	SELECT
		@EpisodeName as [Title],
		@EpisodeID as [Episode ID],
		@NumberCompanions AS [Number of Companions],
		@NumberEnemies AS [Number of Enemies]
END
```

Q. <b>Using variables create a summary output window of aggregated data.</b><br>
```
USE WorldEvents
GO

DECLARE @EventInfo AS varchar(30) = 'Summary of Events'

DECLARE @EarliestDate AS Date = (
	SELECT MIN(EventDate)
		FROM tblEvent )

DECLARE @LatestDate AS Date = (
	SELECT MAX(EventDate)
		FROM tblEvent )

DECLARE @NumberOfEvents as int = (
	SELECT count(*)
		from tblEvent )
SELECT
	@EventInfo AS [Title],
	@EarliestDate AS [Earliest Date],
	@LatestDate AS [Latest Date],
	@NumberOfEvents AS [Number of Events]
```

Q. <b>Filtering a stored procedure using variables.</b><br>
```
USE WorldEvents
GO
DECLARE @DOBYEAR as int = 1991
SELECT 
	EventName, EventDate, CountryName
	FROM tblEvent TE
	INNER JOIN tblCountry TC
		ON TE.CountryID = TC.CountryID
	WHERE
		Year(EventDate) = @DOBYEAR

-- Solution for 2nd Condition
DECLARE @DOBYEAR as int = 1991
DECLARE @DOBFirst as DATE = DATEFROMPARTS(@DOBYEAR,1,1)
DECLARE @DOBLast AS DATE = DATEFROMPARTS(@DOBYEAR,12,31)
SELECT 
	EventName, EventDate, CountryName
	FROM tblEvent TE
	INNER JOIN tblCountry TC
		ON TE.CountryID = TC.CountryID
	WHERE
		EventDate BETWEEN @DOBFirst AND @DOBLast
```

Q. <b>Read a list of the enemies of Doctor Who into a string variable.</b><br>
```
USE DoctorWho
GO
DECLARE @EpisodeID AS int =15
DECLARE @EnemyList AS VARCHAR(100) = ''
SELECT
	-- add in each enemy names
	@EnemyList = @EnemyList + 
		CASE 
			WHEN len(@EnemyList) > 0 THEN ', ' 
			ELSE '' 
		END + 
			TE.EnemyName
			FROM tblEnemy TE
			INNER JOIN tblEpisodeEnemy TEE
				ON TEE.EnemyId = TE.EnemyId
			WHERE
				TEE.EpisodeId = @EpisodeID
-- Printing out the result
SELECT 
	@EpisodeID AS [Episode ID],
	@EnemyList AS [Enemies]
```

Q. <b>Create a list variable to store all the events released in a specified year.</b><br>
```
USE WorldEvents
GO

DECLARE @DOB_YEAR AS int = 2025
DECLARE @Event_list as VARCHAR(max) = ''
DECLARE @NoEvents as VARCHAR(30) = 'No Events for the year'

SELECT 
	TOP 3 @Event_list = @Event_list  + EventName +', '
	from tblEvent
	where Year(eventDate) = @DOB_YEAR
	Order by eventname

IF len(@event_list) = 0 
	SELECT @NoEvents AS [Eventful Year]
else
	select
		@Event_list AS [Eventful Year]
```

Q. <b>Given the name of a Doctor Who, use variables to print details for him.</b><br>
```
USE DoctorWho
GO
-- Doctor number to be between 9,10,11,12 only(given condition)
DROP PROC if exists spSearchDoctorAppearance
GO

CREATE PROC spSearchDoctorAppearance @DoctorNumber AS INT
AS 
BEGIN
	DECLARE @DoctorID AS INT 
	DECLARE @DoctorName As VARCHAR(100)

	SELECT
		@DoctorID = doctorID,
		@DoctorName = DoctorName
		
		FROM tblDoctor
			WHERE DoctorNumber = @DoctorNumber 
	DECLARE @NumberOfEpisodes AS INT = (
		SELECT Count(*)
			from tblEpisode
			WHERE DoctorId = @DoctorID)

	PRINT 'Results for Doctor Number ' + CAST(@DoctorNumber AS VARCHAR(10))
	PRINT '------------------------------------------'
	PRINT ''
	PRINT 'Doctor Name: ' + UPPER(@DoctorName)
	PRINT ''
	PRINT 'Episodes appeared in: ' + CAST(@NumberOfEpisodes AS VARCHAR(10))
	PRINT ''
	PRINT '-------------------------------------------'
END
```

<i>**** -- Module Completed -- ****</i>
