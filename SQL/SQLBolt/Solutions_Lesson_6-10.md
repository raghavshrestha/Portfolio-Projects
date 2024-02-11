Source: @SQLBolt (https://sqlbolt.com/lesson/)

### SQL Lesson 6: Multi-table queries with JOINs
1. Find the domestic and international sales for each movie<br>
```
SELECT m.title, bo.Domestic_sales, bo.International_sales 
FROM movies m
inner join Boxoffice bo ON
m.Id=bo.movie_id;
```
2. Show the sales numbers for each movie that did better internationally rather than domestically<br>
```
SELECT m.title, bo.Domestic_sales,  bo.International_sales
FROM movies m
inner join Boxoffice bo ON
m.Id=bo.movie_id 
where bo.International_sales > bo.Domestic_sales;
```
3. List all the movies by their ratings in descending order<br>
```
select m.title from movies m
inner join Boxoffice bo ON
m.Id=bo.movie_id
Order by bo.rating desc;
```

### SQL Lesson 7: OUTER JOINs
1. Find the list of all buildings that have employees<br>
```
select building from employees group by building; OR
select distinct building from employees;
```
2. Find the list of all buildings and their capacity<br>
```
select * from building;
```
4. List all buildings and the distinct employee roles in each building (including empty buildings)<br>
```
select distinct b.building_name,  e.role from buildings b
left join employees e on
b.building_name=e.building
```

### SQL Lesson 8: A short note on NULLs
1. Find the name and role of all employees who have not been assigned to a building<br>
```
SELECT name, role FROM employees
where building is null;
```
2. Find the names of the buildings that hold no employees<br>
```
SELECT b.building_name from buildings b
left join employees e on
b.building_name = e.building
where e.building is null;
```

### SQL Lesson 9: Queries with Expressions
1. List all movies and their combined sales in millions of dollars<br>
```
SELECT m.title, (bo.Domestic_sales + bo.International_sales)/1000000 AS Total_Sales
 FROM movies m inner join Boxoffice bo ON m.Id=bo.movie_Id;
```
2. List all movies and their ratings in percent<br>
```
SELECT m.title, (bo.rating * 10) AS Rating_percent
FROM movies m inner join Boxoffice bo ON m.Id=bo.movie_Id;
```
3. List all movies that were released on even number years <br>
```
SELECT title from movies
where year%2=0
```
### SQL Lesson 10: Querieswith Aggregates (Pt. 1)
1. Find the longest time that an employee has been at the studio<br>
```SELECT max(years_employed) as Longest_time FROM employees;```
2. For each role, find the average number of years employed by employees in that role<br>
```SELECT role, avg(years_employed) as Avg_Years FROM employees group by role; ```
3. Find the total number of employee years worked in each building <br>
```
SELECT building, SUM(years_employed) as Total_years_employed
FROM employees
GROUP BY building;
```










































