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