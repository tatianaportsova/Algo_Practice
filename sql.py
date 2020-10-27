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

