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
