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