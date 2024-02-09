@Source SQLBolt

### SQL Lesson 1: SELECT queries 101
1. Find the title of each film<br>
   SELECT title FROM movies;
2. Find the director of each film<br>
   SELECT director FROM movies;
3. Find the title and director of each film<br>
   SELECT title, director FROM movies;
4. Find the title and year of each film<br>
   SELECT title, year from movies;
5. Find all the information about each film<br>
   SELECT * from movies;

### SQL Lesson 2: Queries with constraints(Pt. 1)
1. Find the movie with a row ID of 6<br>
   SELECT * from movies where id = 6;
2. Find the movies released in the years between 2000 and 2010<br>
   SELECT * from movies where years between 2000 and 2010
3. Find the movies not released in the years between 2000 and 2010<br>
   SELECT * from movies where year not between 2000 and 2010
4. Find the first 5 Pixar movies and their release year <br>
    SELECT title, year from movies limit 5;

### SQL Lesson 3: Queries with constraints (Pt. 2)
1. Find all the Toy Story movies <br>
    SELECT * from movies where title LIKE '%toy story%';
2. Find all the movies directed by John Lasseter<br>
    SELECT * from movies where director = 'John Lasseter';
3. Find all the movies (and director) not directed by John Lasseter<br>
    SELECT title, director from movies where director <> 'John Lasseter';
4. Find all the WALL-* movies<br>
    SELECT * from movies where title LIKE 'WALL-%';

### SQL Lesson 4: Filtering and Sorting Query results
1. List all the directors of Pixar movies (alphabetically), without duplicates<br>
    SELECT DISTINCT director from movies ORDER BY director ASC;
2. List the last 4 movies released (ordered from most recent to least)<br>
    SELECT title FROM movies ORDER BY year DESC LIMIT 4;
3. List the first 5 Pixar movies sorted alphabetically<br>
    SELECT title FROM movies ORDER BY title LIMIT 5;
4. List the next 5 Pixar movies sorted alphabetically<br>
    SELECT title from movies ORDER BY title LIMIT 5 OFFSET 5;

### SQL Lesson : Simple SELECT Queries
1. List all the Canadian cities and their populations<br>
SELECT city, population FROM north_american_cities
where country='Canada';
2. Order all the cities in the United States by their latitude from north to south<br>
SELECT *FROM north_american_cities
where country='United States' Order by latitude desc;
3. List all the cities west of Chicago, ordered from west to east<br>
SELECT city FROM north_american_cities 
WHERE longitude < -87.629798
ORDER BY longitude
4. List the two largest cities in Mexico (by population)<br>
SELECT city FROM north_american_cities 
where country = 'Mexico'
order by population desc limit 2
5. List the third and fourth largest cities (by population) in the United States and their population<br>
SELECT city FROM north_american_cities 
where country = 'United States'
order by population desc limit 2 offset 2




































  
