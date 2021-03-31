'''
Function Description:
Complete the average function in the editor below.

Average has the following parameters:
- int arr: an array of integers

Returns:
-float: the resulting float value rounded to 3 places after the decimal

Input Format:s
-The first line contains the integer, N, the size of arr.
The second line contains the N space-separated integers, arr[i].
'''

def average(array):
    return round(sum(set(array))/len(set(array)), 3)


'''
Given 2 sets of integers, M and N, print their symmetric difference in ascending order.
The term symmetric difference indicates those values that exist in either M or N
but do not exist in both.
'''

a,b=(int(input()),input().split())
c,d=(int(input()),input().split())
x=set(b)
y=set(d)
p=y.difference(x)
q=x.difference(y)
r=p.union(q)
print ('\n'.join(sorted(r, key=int)))
