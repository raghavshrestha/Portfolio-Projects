
Source: @WiseOwl Training (https://www.wiseowl.co.uk/sql/exercises/standard/setting-criteria-using-where/)

## SQL exercises on SETTING CRITERIA USING WHERE CLAUSE
Q.Write a query to list out all of the events from the tblEvent table in Category number 11 (which corresponds to Love and Relationships, as it happens).<br>
<b>
```
select
  eventName, eventDate
  from tblEvent
  where CategoryId=11;
```
</b>

Q. Create a query which lists out all of the tblEvents which include the word Teletubbies.<br> 
Now add an OR condition to your query so that it lists out all events whose:<br>
  Name includes Teletubbies; or<br>
  Name includes Pandy.
<b>
```
select
eventname,eventdate
from tblevent where eventName LIKE('%Teletubbies%');
OR
select
eventname,eventdate
from tblevent
where eventName LIKE ('%Teletubbies%') OR eventName LIKE('%Pandy%');
```
</b>

Q. 
<b>
```

```
</b>
