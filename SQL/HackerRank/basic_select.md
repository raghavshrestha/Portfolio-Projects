Source: <b>@HackerRank</b> (https://www.hackerrank.com/challenges/)

## Basic Select
#### Problem 1 Weather Observation Station: 
Query the NAME field for all American cities in the CITY table with populations larger than 120000. The CountryCode for America is USA.<br>
```` select NAME from city where COUNTRYCODE='USA' and POPULATION >120000; ````
<br> <br>
Query all columns (attributes) for every row in the CITY table.<br>
``` select * from CITY; ```
<br><br>
Query all columns for a city in CITY with the ID 1661. <br>
``` select * from CITY where ID=1661; ```
<br><br>
Query all attributes of every Japanese city in the CITY table. The COUNTRYCODE for Japan is JPN.<br>
``` select * from CITY where COUNTRYCODE='JPN'; ```
Query the names of all the Japanese cities in the CITY table. The COUNTRYCODE for Japan is JPN.<br>
``` select name from CITY where COUNTRYCODE='JPN'; ```
<br><br>
Query a list of CITY and STATE from the STATION table.<br>
``` select CITY, STATE from STATION; ```
Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order, but exclude duplicates from the answer.<br>
``` select distinct CITY from STATION where id%2=0; ```
<br><br>
Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.<br>
``` select count(city) - count (distinct city) from station; ```
<br><br>
Query the two cities in the station table with the shortest and longest CITY names, as well as their respective lengths(i.e.:number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.<br>
```
select top 1 city, len(city) as length from station order by length ASC, city ASC; 
select top 1 city, len(city) as length from station order by length DESC, city ASC;
```
Query the list of CITY names starting with vowels(i.e., a, e, i, o, u) from STATION. Your result cannot contain duplicates.<br>
``` SELECT DISTINCT CITY FROM STATION WHERE LEFT(CITY,1) IN ('A', 'E',' I', 'O', 'U'); ```
<br><br>
Query the list of CITY names ending with vowels(i.e., a, e, i, o, u) from STATION. Your result cannot contain duplicates.<br>
``` SELECT DISTINCT CITY FROM STATION WHERE RIGHT(CITY,1) IN ('A', 'E',' I',' O','U'); ```
<br><br>
Query the list of CITY names from STATION which have vowels(i.e., a, e, i, o, u) as both their first and last characters. Your result cannot contain duplicates.<br>
``` SELECT DISTINCT CITY FROM STATION WHERE LEFT(CITY,1) IN ('A', 'E',' I',' O', 'U') and RIGHT(CITY,1) IN ('A', 'E',' I',' O', 'U'); ```
<br><br>
Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.<br>
``` SELECT DISTINCT CITY FROM STATION WHERE LEFT(CITY,1) NOT IN ('A', 'E',' I','O', 'U'); ```
<br><br>
Query the list of CITY names from STATION that do not end with vowels. Your result cannot contain duplicates.<br>
``` SELECT DISTINCT CITY FROM STATION WHERE RIGHT(CITY,1) NOT IN ('A', 'E',' I','O', 'U'); ```
<br><br>
Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.<br>
```
SELECT DISTINCT CITY FROM STATION WHERE
LEFT(CITY,1) NOT IN ('A', 'E',' I',' O', 'U') and
RIGHT(CITY,1) NOT IN ('A', 'E',' I',' O', 'U');
```
<br>

#### Problem 2 Higher than 75 Marks: 
Query the name of any student in STUDENTS who scored higher than 75 marks. Order your output by the last three characters of each name. If two or more students both have names ending in the same last three characters(i.e.: Bobby, Robby, etc), secondary sort them by ascending ID.<br>
``` select name from students where marks >75 order by right(name,3) asc, id asc ; ```

#### Problem 3 Employee Table:
Write a query that prints a list of employee names(i.e.: the name attribute) from the Employee table in alphabetical order.<br>
