'''
Function Description:
Complete the average function in the editor below.

Average has the following parameters:
- int arr: an array of integers

Returns:
-float: the resulting float value rounded to 3 places after the decimal

Input Format:
-The first line contains the integer, N, the size of arr.
The second line contains the N space-separated integers, arr[i].
'''

def average(array):
    return round(sum(set(array))/len(set(array)), 3)