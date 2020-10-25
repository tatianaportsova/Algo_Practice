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