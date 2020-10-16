'''
Add up and print the sum 
of the all of the minimum elements of each inner array:

[[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

The expected output is given by:
4 + -1 + 9 + -56 + 201 + 18 = 175

You may use whatever programming language you'd like.
'''
a = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

min_values = []

for i in a:
  min_values.append(min(i))

print(min_values)

total = 0
for i in min_values:
  total += i
print(total)


'''
Add up and print the sum of the all of the minimum elements of each inner array. 
Each array may contain additional arrays nested arbitrarily deep, 
in which case the minimum value for the nested array should be added to the total.

[[8, [4]], 
  [[90, 91], -1, 3], 
  [9, 62], 
  [[-7, -1, [-56, [-6]]]], 
  [201], 
  [[76, 0], 18]]

The expected output for the above input is:
8 + 4 + 90 + -1 + 9 + -7 + -56 + -6 + 201 + 0 + 18 = 260

You may use whatever programming language you'd like.
'''
b = [[8, [4]], [[90, 91], -1, 3], [9, 62], 
     [[-7, -1, [-56, [-6]]]], [201], [[76, 0], 18]]

min_values = [] 

def get_min(data):
    l = []
    for i in range(0, len(data)):
        if type(data[i]) != list:
          l.append(data[i])
          # if i == len(data)-1 or type(data[i+1]) == list:
          #     if len(l) == 1:
          #         min_values.append(l[0])
          #     elif len(l) > 1:
          #        min_values.append(min(l))
        else:
            get_min(data[i])
    
    if l:
      min_values.append(min(l))

get_min(b)
print(min_values)

total = 0
for i in min_values:
    total += i
print(total)