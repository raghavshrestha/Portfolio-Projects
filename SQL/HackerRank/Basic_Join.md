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
hacker earned a full score. If more than one hacker received full scores in the same number of challenges, then sort them by ascending hacker_id.<br>
```
select h.hacker_id, h.name from  submissions s
inner join hackers h on h.hacker_id = s.hacker_id
inner join challenges c on c.challenge_id = s.challenge_id
inner join difficulty d on d.difficulty_level = c.difficulty_level and d.score= s.score
group by h.hacker_id, h.name
having count(h.hacker_id)>1
order by  count(h.hacker_id) desc, h.hacker_id asc;
```
#### Problem 6 Ollivander's Inventory (https://www.hackerrank.com/challenges/harry-potter-and-wands/problem)
Write a query to print the id, age, coins_needed, and power of the wands that Ron's interested in, sorted in order of descending power. If more than one wand has the same power, sort the result in order of descending age. <br>
```
SELECT w.id, wp.age,w.coins_needed,w.power 
FROM Wands w 
JOIN Wands_Property wp on w.code =wp.code 
AND
w.coins_needed IN
(SELECT MIN(w2.coins_needed)FROM Wands w2 
 INNER JOIN Wands_Property wp2 ON w2.code = wp2.code 
 WHERE wp2.is_evil = 0 AND wp.age =wp2.age 
 AND 
 w.power = w2.power) 
 ORDER BY w.power desc, wp.age desc;
```
#### Problem 7 Challenges:
Write a query to print the hacker_id, name, and the total number of challenges created by each student. Sort your results by the total number of challenges in descending order. If more than one student created the same number of challenges, then sort the result by hacker_id. If more than one student created the same number of challenges and the count is less than the maximum number of challenges created, then exclude those students from the result.<br>
```
with challenges_created as (
select h.hacker_id, h.name, count(c.hacker_id) as Challenges_Create from hackers h
join challenges c on c.hacker_id= h.hacker_id
group by c.hacker_id,h.hacker_id,h.name
)
select hacker_id, name, Challenges_Create
from challenges_created
where
Challenges_Create = (select max(Challenges_Create) from challenges_created) OR
Challenges_Create in (select Challenges_Create from Challenges_created
                     group by Challenges_Create
                     having count(Challenges_Create) = 1 )
order by Challenges_Create desc, hacker_id asc;
```






















