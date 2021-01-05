"""
Given an integer, n, and n space-separated integers as input, 
create a tuple, t, of those n integers. 
Then compute and print the result of hash(t).

Note: hash() is one of the functions in the __builtins__ module, 
so it need not be imported.
"""

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))


"""
Given the names and grades for each student in a class of N students, 
store them in a nested list and print the name(s) of any student(s) 
having the second lowest grade.

Note: If there are multiple students with the second lowest grade, 
order their names alphabetically and print each name on a new line.
"""

if __name__ == '__main__':
    names = []
    scores = []
    for _ in range(int(input())):
        name = input()
        names.append(name)        
        score = float(input())
        scores.append(score)   
    min_ = scores.index(min(scores))
    del names[min_]
    del scores[min_]
    
    new_min = scores[scores.index(min(scores))]
    names_ = []
    for i in range(0,len(scores)):
        if scores[i] == new_min:
            names_.append(names[i])
            
    for i in sorted(names_):
        print(i)

# Better Solution:

if __name__ == '__main__':
    marksheet = []
    for _ in range(0,int(input())):
        marksheet.append([input(), float(input())])

    second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
    print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))


"""
You are given a string s consisting only of digits 0-9, commas ,, and dots .

Your task is to complete the regex_pattern defined below, 
which will be used to re.split() all of the , and . symbols in s.

It’s guaranteed that every comma and every dot in s is preceeded and followed by a digit.
"""

regex_pattern = r",|\."	

import re
print("\n".join(re.split(regex_pattern, input())))

"""
HackerLand University has the following grading policy:

Every student receives a grade in the inclusive range from 0 to 100.
Any grade less than 40 is a failing grade.
Sam is a professor at the university and likes to round each student's grade according to these rules:

If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
"""

def gradingStudents(grades):
    for g in range(0, len(grades)):
        if grades[g] >= 38:
            if (grades[g]+1)%5 == 0:
                grades[g] = grades[g]+1
            elif (grades[g]+2)%5 == 0:
                grades[g] = grades[g]+2
    return grades

"""
Sam's house has an apple tree and an orange tree that yield an abundance of fruit. 
Using the information given below, determine the number of apples and oranges that land on Sam's house.

In the diagram below:

The red region denotes the house, where s is the start point, and t is the endpoint. 
The apple tree is to the left of the house, and the orange tree is to its right.
Assume the trees are located on a single point, where the apple tree is at point a, 
and the orange tree is at point b.
When a fruit falls from its tree, it lands d units of distance from its tree of origin 
along the -axis. *A negative value of d means the fruit fell d units to the tree's left,
 and a positive value of d means it falls d units to the tree's right. *
 """

 def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_ = 0
    for i in apples:
        if (i+a)>=s and (i+a)<=t:
            apples_ += 1
    oranges_ = 0
    for i in oranges:
        if (i+b)>=s and (i+b)<=t:
            oranges_ += 1
    print(apples_)
    print(oranges_)


"""
You are given a string and your task is to swap cases. In other words, 
convert all lowercase letters to uppercase letters and vice versa.
"""

def swap_case(s):
    return s.swapcase()

"""
You are given a string. 
Split the string on a " " (space) delimiter and join using a - hyphen.
"""

def split_and_join(line):
    line = line.split(" ")
    return "-".join(line)


"""
In Python, a string of text can be aligned left, right and center.

You are given a partial code that is used for generating the HackerRank Logo of variable thickness.
Your task is to replace the blank (______) with rjust, ljust or center.
"""

#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

"""
You are asked to ensure that the first and last names of people begin 
with a capital letter in their passports. 
For example, alison heck should be capitalised correctly as Alison Heck.
"""

def solve(s):
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


"""
You are given an integer, N. Your task is to print an alphabet rangoli of size N. 
(Rangoli is a form of Indian folk art based on creation of patterns.)
"""

import string

def print_rangoli(size):
    alpha = string.ascii_lowercase

    L = []
    for i in range(size):
        s = "-".join(alpha[i:size])
        L.append((s[::-1]+s[1:]).center(4*size-3, "-"))
    print('\n'.join(L[:0:-1]+L))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)





