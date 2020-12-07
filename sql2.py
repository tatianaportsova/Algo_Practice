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