Source: @Wiseowl<br>
SQL exercises on [TESTING CONDITIONS](https://www.wiseowl.co.uk/sql/exercises/standard/testing-conditions/)

Q. <b>Use IF to change the SELECT statement that a stored proc runs.</b><br>
```
use WorldEvents
go

drop proc if exists uspInformation
go

create proc uspInformation @info as VARCHAR(20)=NULL
as

if @info = 'Event'
begin
	select Top 2 EventName, EventDetails,EventDate from tblEvent
end
else if @info = 'Country'
begin
	select Top 2 countryName from tblCountry
end
else if @info = 'Continent'
begin
	select Top 2 ContinentName from tblContinent
end
if @info not in('Event','Country','Continent') or @info is null
begin
	select 'You must enter: Event, Country or Continent' AS [Nuh uh say the magic word]
```
<i>**** --- Module Completed --- ****</i>
