Source: <b>@HackerRank</b> (https://www.hackerrank.com/challenges/)

## Basic Joins
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
select 
case
when g.grade < 8 then NULL
else s.name
end,
g.grade,s.marks from students s
inner join grades g on
s.marks between g.min_mark and g.max_mark
order by  g.grade desc, s.name asc;
```
#### Problem 5 Top Competitors (https://www.hackerrank.com/challenges/full-score/problem)
Julia just finished conducting a coding contest, and she needs your help assembling the leaderboard! Write a query to print the respective hacker_id and name of hackers who achieved full scores for more than one challenge. Order your output in descending order by the total number of challenges in which the
hacker earned a full score. If more than one hacker received full scores in same number of challenges, then sort them by ascending hacker_id.<br>
