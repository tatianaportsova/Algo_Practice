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