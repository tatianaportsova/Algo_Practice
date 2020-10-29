'''
select distinct city from station where city REGEXP "^[aeiou].*";
'''

'''
select distinct city from station where SUBSTR(city,-1,1) in ('a','e','i','o','u');
'''

'''
select distinct city
    from station where SUBSTR(city,1,1) in ('A','E','I','O','U') and 
    SUBSTR(city,-1,1) in ('a','e','i','o','u');
'''

'''
select distinct city from station where substr(city,-1,1) not in ('a','e','i','o','u');
'''

'''
select distinct city 
    from station where substr(city, 1,1) not in ('A', 'E', 'I', 'O', 'U') or substr(city, -1,1)             not in ('a', 'e', 'o', 'u', 'i');
'''

'''
Query the Name of any student in STUDENTS who scored higher than 75 Marks. 
Order your output by the last three characters of each name. 
If two or more students both have names ending in the same last three characters 
(i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.

select name from students where marks > 75 order by substr(name, -3) asc;
'''

'''
Write a query that prints a list of employee names (i.e.: the name attribute) 
for employees in Employee having a salary greater than $2000 per month 
who have been employees for less than 10 months. Sort your result by ascending employee_id.

select name from employee where salary > 2000 and months < 10 order by employee_id asc;
'''

'''
Query the greatest value of the Northern Latitudes (LAT_N) from STATION that is less than 137.2345.
Truncate your answer to 4 decimal places.

select cast(max(lat_n) as decimal(10,4)) from station where lat_n < 137.2345;
'''

'''
Query the Western Longitude (LONG_W) for the largest Northern Latitude (LAT_N) in STATION 
that is less than 137.2345.
Round your answer to 4 decimal places.

Select ROUND(LONG_W,4) from STATION WHERE LAT_N = (SELECT MAX(LAT_N) FROM STATION WHERE LAT_N<137.2345);
'''

'''
Query the smallest Northern Latitude (LAT_N) from STATION that is greater than 38.7780.
Round your answer to 4 decimal places.

select round(min(lat_n),4) from station where lat_n > 38.7780;
'''

'''
Query the sum of the populations for all Japanese cities in CITY. 
The COUNTRYCODE for Japan is JPN.

select sum(population) from city where countrycode = 'JPN';
'''

'''
Consider P1(a,b) and P2(c,d) to be two points on a 2D plane.
a happens to equal the minimum value in Northern Latitude (LAT_N in STATION).
b happens to equal the minimum value in Western Longitude (LONG_W in STATION).
b happens to equal the maximum value in Northern Latitude (LAT_N in STATION).
d happens to equal the maximum value in Western Longitude (LONG_W in STATION).
Query the Manhattan Distance between points  and  and round it to a scale of  decimal places.


select round((max(lat_n)-min(lat_n))+(max(long_w)-min(long_w)),4) from station;
'''

'''
Consider P1(a,b) and P2(c,d) to be two points on a 2D plane 
where (a,b) are the respective minimum and maximum values of Northern Latitude (LAT_N) 
and (c,d) are the respective minimum and maximum values of Western Longitude (LONG_W) in STATION.
Query the Euclidean Distance between points P1 and P2 and format your answer to display  decimal digits.

select round(sqrt(power(max(lat_n)-min(lat_n), 2)+power(max(long_w)-min(long_w), 2)), 4)from station;
'''

'''
Write a query identifying the type of each record in the TRIANGLES table using its three side lengths. Output one of the following statements for each record in the table:

Equilateral: It's a triangle with 3 sides of equal length.
Isosceles: It's a triangle with 2 sides of equal length.
Scalene: It's a triangle with 3 sides of differing lengths.
Not A Triangle: The given values of A, B, and C don't form a triangle.

SELECT CASE
WHEN A + B > C THEN CASE WHEN A = B AND B = C THEN 'Equilateral' WHEN A = B OR B = C OR A = C THEN 'Isosceles' WHEN A != B OR B != C OR A != C THEN 'Scalene' END
ELSE 'Not A Triangle' END FROM TRIANGLES;
'''

'''
Query an alphabetically ordered list of all names in OCCUPATIONS, 
immediately followed by the first letter of each profession as a parenthetical 
(i.e.: enclosed in parentheses). 
For example: AnActorName(A), ADoctorName(D), AProfessorName(P), and ASingerName(S).
Query the number of ocurrences of each occupation in OCCUPATIONS. 
Sort the occurrences in ascending order, and output them in the following format:

There are a total of [occupation_count] [occupation]s.

where [occupation_count] is the number of occurrences of an occupation in OCCUPATIONS 
and [occupation] is the lowercase occupation name. 
If more than one Occupation has the same [occupation_count], they should be ordered alphabetically.


SELECT Name || '(' || SUBSTR(Occupation, 1, 1) || ')'
FROM OCCUPATIONS
ORDER BY Name;

SELECT 'There are a total of ' || Count(Name) || ' ' || LOWER(Occupation) || 's.'
FROM Occupations
GROUP BY Occupation
ORDER BY Count(Name), Occupation;
'''