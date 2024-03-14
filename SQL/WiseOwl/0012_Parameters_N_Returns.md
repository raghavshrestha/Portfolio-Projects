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
USE WorldEvents
GO
CREATE PROC	uspContinentEvents
	(@Con_Name AS VARCHAR(50) = NULL,
	@After DATETIME = NULL,	@Before DATETIME = NULL)
AS
BEGIN
	SELECT 
		TC.ContinentName, TE.EventName, TE.EventDate
		FROM tblContinent TC
		INNER JOIN tblCountry TCO ON TCO.ContinentID = TC.ContinentID
		INNER JOIN TBLEVENT TE ON TCO.CountryID = TE.CountryID
		WHERE 
			(TC.ContinentName = @CON_NAME OR @CON_NAME IS NULL) AND
			(TE.EventDate >= @After OR @After IS NULL) AND
			(TE.EventDate <= @Before OR @Before IS NULL)
END
```

Q. <b> Filter in a stored procedure using a parameter.</b><br>
```
USE WorldEvents
GO
CREATE PROC spCountryEvents
	(@Country_Name AS VARCHAR(20) = NULL)
AS
BEGIN
SELECT 
	TE.EVENTNAME, TE.EventDate, TC.CountryName
	FROM tblEvent TE
	INNER JOIN tblCountry TC ON TC.CountryID = TE.CountryID
	WHERE 
		TC.CountryName LIKE '%' + @Country_Name + '%' OR
		@Country_Name IS NULL
END
```

Q. <b>Use an output parameter to return a list variable of the most eventful continents. </b><br>
```
USE WorldEvents
GO
DECLARE @CON_NAME AS VARCHAR(MAX) =''
SELECT
	@CON_NAME = @CON_NAME + 
		CASE 
			WHEN LEN(@CON_NAME) > 0 THEN ' ' 
			-- can include ', ' to separate continent name but have used
			-- space in between
			ELSE ''
		END +		
		ContinentName
		FROM tblContinent TC
		INNER JOIN tblCountry TCC
			ON TCC.ContinentID = TC.ContinentID
		INNER JOIN tblEvent TE
			ON TE.CountryID = TCC.CountryID
			GROUP BY CONTINENTNAME
			HAVING COUNT(*) >= 50
SELECT left(@CON_NAME,len(@con_name)-1) AS [Big Happenings]
```

Q. <b>Use return values to bring back an INT return value from a stored procedure. </b><br>
```
use WorldEvents
go
create proc uspHowMuchLonger
AS
declare @difference int = 0
BEGIN
	select 
		@difference = max(len(eventname)) - min(len(eventname))
		from tblEvent
	RETURN @difference
END
declare @diff AS int
exec @diff = uspHowMuchLonger
print @diff
```

Q. <b>Count rows and pass the information out of a procedure using output parameters. </b><br>
```
use DoctorWho
go
drop proc if exists spGoodAndBad
GO
create proc spGoodAndBad
AS
declare @SeriesNumber int = 1

declare @NumEnemies int =
	( Select count(distinct(tee.EnemyId))
		from tblEpisodeEnemy TEE
		inner join tblEpisode TE
		ON te.EpisodeId = tee.EpisodeId
		where TE.SeriesNumber = @SeriesNumber )

declare @NumCompanions int = 
	( select count(distinct(tec.CompanionId))
		from tblEpisodeCompanion TEC
		inner join tblEpisode te
		on te.EpisodeId = TEC.EpisodeId
		where TE.SeriesNumber = @SeriesNumber )

select
	@SeriesNumber AS [Series Number],
	@NumEnemies AS [Number of Enemies],
	@NumCompanions AS [Number of Companions]
```

Q. <b>Return a continent name from one procedure, and pass the output value into another. </b><br>
```
use WorldEvents
go
drop proc if exists spContinentName
go
create proc spContinentName
( @First_Con_name as VARCHAR(30) = null output)
AS
BEGIN
select 
	top 1 @First_Con_name = tc.ContinentName
	from tblEvent te
	inner join tblCountry tcc
		on tcc.CountryID = te.CountryID
	inner join tblContinent tc
	on tc.ContinentID = tcc.ContinentID
	order by te.EventDate asc
END
-- 2nd Statement
drop proc if exists spContinentEvents
go
create proc spContinentEvents @Con_name AS VARCHAR(30) = NULL
AS
BEGIN
	select 
	te.EventName, te.EventDate,tc.ContinentName
	from tblEvent te
	inner join tblCountry tcc
		on tcc.CountryID = te.CountryID
	inner join tblContinent tc
	on tc.ContinentID = tcc.ContinentID
	where tc.ContinentName = @Con_name or
	@Con_name is null

END
-- Verifying the script execution and results if satisfied
declare @var varchar(100)=''
exec spContinentName
@First_Con_name = @var OUTPUT
select @var
exec spContinentEvents 
@Con_name = @var
```

Q. <b>Return from a stored proecure the name of the country with the most events and how many events there were. </b><br>
```
```
<i> **** --- Module Completed --- ****</i>
