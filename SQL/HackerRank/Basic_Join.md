Source: <b>@HackerRank</b> (https://www.hackerrank.com/challenges/)

## Basic Select
#### Problem 1 Population Census: 
Given the CITY and COUNTRY tables, query the sum of the populations of all cities where the CONTINENT is 'Asia'.<br>
```
select sum(c1.population) from city c1
inner join country c2 on
c1.countrycode = c2.code 
where c2.continent = 'Asia'
group by c2.continent;
```
#### Problem 2 African Cities:
Given the CITY and COUNTRY tables, query the names of all cities where the continent is 'Africa'.<br>
```
select c1.name from city c1
inner join country c2 on
c1.countrycode = c2.code
where c2.continent = 'Africa';
```
#### Problem 3 Average Population of Each Continent:
Given the CITY and COUNTRY tables, query the names of all the continents(COUNTRY.Continent) and their respective average
city populations(CITY.population) rounded down to the nearest integer.<br>
```
select c2.Continent, round(avg(c1.population),0) from Country c2
inner join city c1 on
c1.countrycode = c2.code
group by c2.continent;
```
#### Problem 4 The Report:
Ketty gives Eve a task to generate a report containing three columns: NAME, GRADE, and MARK. Ketty doesn't want
the NAMES of those students who received a grade lower than 8. The report must be in descending order by GRADE -- 
i.e. higher GRADES are entered first. If there is more than one student with the same GRADE(8-10) assigned to them, 
order those particular students by their name alphabetically. Finally, if the GRADE is lower than 8, use "NULL"
as their NAME and list them by their GRADES in descending order. If there is more than one student with the  same
GRADE(1-7) assigned to them, order those particular students by their MARKS in ascending order.<br>
Write a query to help Eve.<br>
```
```
