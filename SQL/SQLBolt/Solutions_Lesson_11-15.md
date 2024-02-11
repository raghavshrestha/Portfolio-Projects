Source: @SQLBolt (https://sqlbolt.com/lesson/)

### SQL Lesson 11: Queries with Aggregates (Pt. 2)
1. Find the number of Artists in the studio (without a HAVING clause)<br>
```SELECT count(*) FROM employees where role='Artist';```
2. Find the number of Employees of each rol in the studio<br>
```SELECT role, count(*) FROM employees group by role;```
3. Find the total number o years employed by all Engineers<br>
```
SELECT role, SUM(years_employed)
FROM employees
GROUP BY role
HAVING role = "Engineer";
```

### SQL Lesson 12: Order of execution of a Query
1. Find the number of movies each director has directed<br>
``` SELECT director, count(*) FROM movies group by director; ```
2. Find the total domestic and international sales that can be attributed to each director <br>
```
SELECT director, sum(bo.domestic_sales + bo.international_sales) AS Combined_Sales
FROM movies m inner join Boxoffice bo ON
m.Id=bo.movie_Id
group by director;
```

### SQL Lesson 13: Inserting rows
1. Add the studio's new production, Toy Story 4 to the list of movies (you can use any director)<br>
``` insert into Movies (title, director, year) values('Toy Story 4','John Lasseter', 2024);```
2. Toy Story 4 has been released to critical acclaim! It had a rating of 8.7, and made 340 million domestically and 270 million internationally. Add the record to the Boxoffice table. <br>
``` insert into Boxoffice values (15,8.7,340000000,270000000);```

### SQL Lesson 14: Updating rows
1. The director for A Bug's Life is incorrect, it was actually directed by "John Lasseter".<br>
```
select id from movies where  title="A Bug's Life";
update movies set director='John Lasseter' where id=2;
```
3. The year that Toy Story 2 was released is incorrect, it was actually released in 1999.<br>
```
select id from movies where  title="Toy Story 2";
update movies set year=1999 where id=3;
```
5. Both the title and director for Toy Story 8 is incorrect! The title should be "Toy Story 3" and it was directed by "Lee Unkrich". <br>
```
select id from movies where  title="Toy Story 8"; 
update movies set title = "Toy Story 3", director="Lee Unkrich"
where id=11;
```

### SQL Lesson 15: Deleting rows
1. This database is getting too big, lets remove all movies that were released before 2005.<br>
``` delete from movies where year <= 2005; ```
2. Andrew Stanton has also left the studio, so please remove all movies directed by him. <br>
``` delete from movies where director='Andrew Stanton'; ```
