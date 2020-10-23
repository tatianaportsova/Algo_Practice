'''
select distinct city from station where city REGEXP "^[aeiou].*";
'''

'''
select distinct city from station where SUBSTR(city,-1,1) in ('a','e','i','o','u');
'''