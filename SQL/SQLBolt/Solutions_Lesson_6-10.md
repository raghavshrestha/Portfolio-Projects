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
