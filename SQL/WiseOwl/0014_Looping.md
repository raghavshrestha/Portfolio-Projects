Source: @Wiseowl<br>
SQL exercises on [LOOPING](https://www.wiseowl.co.uk/sql/exercises/standard/looping/)

Q.<b> Create a loop to perform a count for each year of a given range.</b><br>
```
use WorldEvents
go

create proc spYearLooping
as
declare @start_year as int = (select year(min(eventdate)) from tblEvent)
declare @end_year as int = (select year(max(eventdate)) from tblEvent)
while @start_year <= @end_year
begin
	declare @count_events as int = 
		(select count(*) from tblEvent where year(eventdate) = @start_year)
	if @count_events !=0 -- only printing year with events
		print cast(@count_events as varchar(10)) + ' events occurred in ' + cast(@start_year as varchar(10))
	set @start_year +=1
end
```

Q.<b>Use a loop to show a comma-delimited list of all the films released in each month. </b><br>
```

```

Q.<b>Write a nested WHILE loop to find the first N primes. </b><br>
```
```
