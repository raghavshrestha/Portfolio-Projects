Source: <b>@SQLBolt</b> (https://sqlbolt.com/lesson/)

### SQL Lesson 16: Creating tables
1. Create a new table named Database with the following columns:
   -> Name A string(text) describing the name of the database.
   -> Version A number(floating point) of the latest version of this database.
   -> Download_count An integer count of the number of times this database was downloaded.
   This table has no constraints.
```
create table Database (
Name TEXT,
Version FLOAT,
Download_count INTEGER);
```
### SQL Lesson 17: Altering tables
1. Add a column named Aspect_ratio with a FLOAT data type to store the aspect-ratio each movie was released in.<br>
``` alter table movies add Aspect_ratio FLOAT; ```
2. Add another column named Language with a TEXT data type to store the language that the movie was released in. Ensure that the default for this language is English.<br>
``` alter table movies add Language TEXT default 'English'; ```
