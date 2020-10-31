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