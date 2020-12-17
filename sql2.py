'''
Query the following two values from the STATION table:

The sum of all values in LAT_N rounded to a scale of 2 decimal places.
The sum of all values in LONG_W rounded to a scale of 2 decimal places.

select round(sum(lat_n), 2), round(sum(long_w), 2) from station;
'''

'''
Query the sum of Northern Latitudes (LAT_N) from STATION having values 
greater than 38.7880 and less than 137.2345. Truncate your answer to 4 decimal places.

select round(sum(lat_n), 4) from station where lat_n>38.7880 and lat_n<137.2345;
'''

'''
A median is defined as a number separating the higher half of a data set 
from the lower half. 
Query the median of the Northern Latitudes (LAT_N) from STATION 
and round your answer to 4 decimal places.

select round(s.lat_n, 4) from station as s where (select count(lat_n) from station where lat_n < s.lat_n) = (select count(lat_n) from station where lat_n > s.lat_n)
'''

'''
Query the difference between the maximum and minimum populations in CITY.

select max(population)-min(population) as difference from city;
'''

'''
Samantha was tasked with calculating the average monthly salaries for all employees 
in the EMPLOYEES table, but did not realize her keyboard's 0 key was broken until after 
completing the calculation. 
She wants your help finding the difference between her miscalculation 
(using salaries with any zeroes removed), and the actual average salary.

Write a query calculating the amount of error (i.e.: actual-miscalculated average monthly salaries), 
and round it up to the next integer.

select ceil(avg(salary)-avg(replace(salary, '0',''))) from employees;

The CEIL() function returns the smallest integer value that is bigger than or equal to a number.

Note: This function is equal to the CEILING() function.
'''

'''
We define an employee's total earnings to be their monthly salary*months worked, 
and the maximum total earnings to be the maximum total earnings for any employee 
in the Employee table. 
Write a query to find the maximum total earnings for all employees as well as 
the total number of employees who have maximum total earnings. 
Then print these values as 2 space-separated integers.

select (salary * months)as earnings, count(*) from employee group by 1 order by earnings desc limit 1;
'''

'''
Given the CITY and COUNTRY tables, query the sum of the populations of all cities where the CONTINENT is 'Asia'.

select sum(city.population) from city
join country on city.countrycode=country.code
where country.continent='Asia';
'''

'''
Given the CITY and COUNTRY tables, query the names of all cities where the CONTINENT is 'Africa'.
Note: CITY.CountryCode and COUNTRY.Code are matching key columns.

select city.name from city
join country on city.countrycode=country.code
where country.continent='Africa';
'''


'''
Given the CITY and COUNTRY tables, query the names of all the continents 
(COUNTRY.Continent) and their respective average city populations (CITY.Population) 
rounded down to the nearest integer.

select country.continent, floor(avg(city.population)) from city
join country on city.countrycode=country.code
group by country.continent;
'''
# ROUND - Rounds a positive or negative value to a specific length 
# and accepts three values:
#   - Value to round
#      - Positive or negative number
#      - This data type can be an int (tiny, small, big), decimal, numeric, money or smallmoney
#   - Precision when rounding
#      - Positive number rounds on the right side of the decimal point
#      - Negative number rounds on the left side of the decimal point
#   -Truncation of the value to round occurs when this value is not 0 or not included

# CEILING - Evaluates the value on the right side of the decimal 
# and returns the smallest integer greater than, or equal to, 
# the specified numeric expression and accepts one value:
#   - Value to round

# FLOOR - Evaluates the value on the right side of the decimal 
# and returns the largest integer less than or equal 
# to the specified numeric expression and accepts one value: 
#   - Value to round

'''
Harry Potter and his friends are at Ollivander's with Ron, 
finally replacing Charlie's old broken wand. Hermione decides the best way to choose 
is by determining the minimum number of gold galleons needed to buy each non-evil wand 
of high power and age. 
Write a query to print the id, age, coins_needed, and power of the wands that Ron's 
interested in, sorted in order of descending power. 
If more than one wand has same power, sort the result in order of descending age.

select max(wands.power) from wands
join wands_property on wands.code=wands_property.code
where wands_property.is_evil=0;
'''

'''
P(R) represents a pattern drawn by Julia in R rows. The following pattern represents P(5):

* * * * * 
* * * * 
* * * 
* * 
*
Write a query to print the pattern P(20).

SELECT REPEAT('* ', @NUMBER := @NUMBER - 1) FROM information_schema.tables, (SELECT @NUMBER:=21) t LIMIT 20;
'''

'''
P(R) represents a pattern drawn by Julia in R rows. The following pattern represents P(5):

* 
* * 
* * * 
* * * * 
* * * * *
Write a query to print the pattern P(20).

select REPEAT('* ', @i := @i + 1) from information_schema.tables, (select @i := 0) t LIMIT 20;
'''