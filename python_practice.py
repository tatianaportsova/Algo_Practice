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