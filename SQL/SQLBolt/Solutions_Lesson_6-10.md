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
