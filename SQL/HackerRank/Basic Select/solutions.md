Source: <b>@HackerRank</b> (https://www.hackerrank.com/challenges/)


#### Problem 1: 
Query the NAME field for all American cities in the CITY table with populations larger than 120000. The CountryCode for America is USA.<br>
```` select NAME from city where COUNTRYCODE='USA' and POPULATION >120000; ````

#### Problem 2: 
Query all columns (attributes) for every row in the CITY table.<br>
``` select * from CITY; ```

#### Problem 3:
Query all columns for a city in CITY with the ID 1661. <br>
``` select * from CITY where ID=1661; ```

#### Problem 4:
Query all attributes of every Japanese city in the CITY table. The COUNTRYCODE for Japan is JPN.<br>
``` select * from CITY where COUNTRYCODE='JPN'; ```
Query the names of all the Japanese cities in the CITY table. The COUNTRYCODE for Japan is JPN.<br>
``` select name from CITY where COUNTRYCODE='JPN'; ```

#### Problem 5:
Query a list of CITY and STATE from the STATION table.<br>
``` select CITY,STATE from STATION; ```
Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order, but exclude duplicates from the answer.<br>
``` select distinct CITY from STATION where id%2=0; ```

#### Problem 6:
#### Problem 7:
#### Problem 8:
#### Problem 9:
#### Problem 10:
