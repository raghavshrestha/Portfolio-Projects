
Source @WiseOwl (https://www.wiseowl.co.uk/sql/exercises/standard/more-exotic-joins/)<br>

## SQL exercises on MORE EXOTIC JOINS

Q. <b>Write an SQL outer join to show unmatched records in another table. </b><br>
Create a query based on the companions table, with an outer join to the episode companion table.
```
SELECT        
	tc.CompanionName
	FROM tblCompanion tc 
	FULL OUTER JOIN tblEpisodeCompanion tec
		ON tc.CompanionId = tec.CompanionId
	FULL OUTER JOIN tblEpisode te
		ON tec.EpisodeId =te.EpisodeId
	where te.EpisodeType is null
```

Q. <b> Create 2 self-joins between a table of families and itself, to show families, their parents and their grandparents</b><br>

```
SELECT 
    F.[FamilyName],
    ISNULL('All categories' + ' > ' +
    IIF(PF.FamilyId = 25,'',PF.[FamilyName]) + ' > ' +
    TF.[FamilyName], 'All categories') AS 'Family path'
FROM
    tblFamily AS F
    LEFT JOIN tblFamily AS PF
        ON F.ParentFamilyId = PF.FamilyID    
    LEFT JOIN tblFamily AS TF
        ON F.FamilyId = TF.FamilyID    
ORDER BY
    F.[FamilyName]
```

<i>**** Moddule Completed ****
