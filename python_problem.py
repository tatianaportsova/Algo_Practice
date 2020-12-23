'''
Given a square matrix, 
calculate the absolute difference between the sums of its diagonals.

Sample Input:

11 2 4
4 5 6
10 8 -12 

Return the absolute difference between the sums of the matrix's two diagonals 
as a single integer.

Sample Output:

15

'''


def diagonalDifference(arr):
    l = len(arr)
    primary = []
    secondary = []
    i = 0
    p = 0
    s = l-1
    while i < l:
        primary.append(arr[i][p])
        secondary.append(arr[i][s])
        p += 1
        s -= 1
        i += 1

    return abs(sum(primary)-sum(secondary))


'''
Given five positive integers, find the minimum and maximum values 
that can be calculated by summing exactly four of the five integers. 
Then print the respective minimum and maximum values as a single line 
of two space-separated long integers.

Sample Input:

[1, 2, 3, 4, 5]

Sample Output:

10, 14

'''

def miniMaxSum(arr):
    min_ = 0
    max_ = 0
    for i in arr:
        if i != min(arr):
            max_ += i
        if i != max(arr):
            min_ += i
        
    print(min_, max_)


def miniMaxSum(arr):
    max=-sys.maxsize-1
    min=sys.maxsize
    sum=0
    for x in arr:
        sum+=x
        if x>max:
            max=x
        if x<min:
            min=x
    print (sum-max,sum-min)


"""
Given the names and grades for each student in a class of N students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, 
order their names alphabetically and print each name on a new line.
"""

l = []
scores = []

if __name__ == '__main__':
    for _ in range(int(input())):
        student = []
        name = input()
        score = float(input())
        scores.append(score)
        student.append(name)
        student.append(score)
        l.append(student)

scores.remove(min(scores))
names = []

for i in l:
    if i[1] == min(scores):
        names.append(i[0])
        
for i in sorted(names):
    print(i)


"""
Lilah has a string, s, of lowercase English letters that she repeated infinitely many times.

Given an integer, n, find and print the number of letter a's in the first n letters of Lilah's infinite string.

For example, if the string s='abcac' and n=10, the substring we consider is abcacabcac, 
the first 10 characters of her infinite string. There are 4 occurrences of a in the substring.
"""

def repeatedString(s, n):
    # if len(s)<n:
    #     while len(s)<n:
    #         s = s+s
    
    # return s[:n].count('a')
    return s.count("a") * (n // len(s)) + s[:n % len(s)].count("a")


"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a new line with  places after the decimal.
"""

def plusMinus(arr):
    pos = 0
    neg = 0
    net = 0
    for i in arr:
        if i>0:
            pos += 1
        elif i==0:
            net += 1
        else:
            neg += 1
            
    print(pos/len(arr))
    print(neg/len(arr))
    print(net/len(arr))


'''
The provided code stub will read in a dictionary containing key/value pairs 
of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, 
showing 2 places after the decimal.
'''

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    p =  sum(student_marks[query_name])/3
    print(format(p, '.2f'))


"""
You are given the firstname and lastname of a person on two different lines. 
Your task is to read them and print the following:
  Hello firstname lastname! You just delved into python.
"""

def print_full_name(a, b):
    print "Hello {} {}! You just delved into python.".format(a,b)


"""
We have seen that lists are mutable (they can be changed), 
and tuples are immutable (they cannot be changed).
You are given an immutable string, and you want to make changes to it.
"""

def mutate_string(string, position, character):
    return string[:position] + str(character) + string[position+1:]


"""
In this challenge, the user enters a string and a substring. 
You have to print the number of times that the substring occurs in the given string. 
String traversal will take place from left to right, not from right to left.
NOTE: String letters are case-sensitive.
"""

def count_substring(string, sub_string):
    count_ = 0
    if len(sub_string) > len(string):
        return count_
    elif len(sub_string) <= len(string):
        start = 0
        while start < len(string) and start+(len(sub_string)+1) <= len(string)+1:
            if string[start:start+len(sub_string)] == sub_string:
                count_ += 1
            start += 1

    return count_

"""
You are given a string .
Your task is to find out if the string  contains: alphanumeric characters, 
alphabetical characters, digits, lowercase and uppercase characters.

In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
In the second line, print True if S has any alphabetical characters. Otherwise, print False.
In the third line, print True if S has any digits. Otherwise, print False.
In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
In the fifth line, print True if S has any uppercase characters. Otherwise, print False.
"""

if __name__ == '__main__':
    s = raw_input()
    print(s.isalnum())
    if not s.isdigit():
        print(True)
    if not s.isalpha():
        print(True)
    if not s.isupper():
        print(True)
    if not s.islower():
        print(True)