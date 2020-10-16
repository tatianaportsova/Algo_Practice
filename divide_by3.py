'''
Print out all of the numbers in the following array that are divisible by 3:
[85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]

The expected output for the above input is:
27
81
9
27
99
63
42

You may use whatever programming language you wish.
'''
a = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]

for i in a:
  if i % 3 == 0:
    print(i)

'''
Print out all of the strings in the following array that represent a number divisible by 3:
["five","twenty six","nine hundred ninety nine","twelve","eighteen",
  "one hundred one","fifty two","forty one","seventy seven",
  "six","twelve","four","sixteen"]

The expected output for the above input is:
nine hundred ninety nine
twelve
eighteen
six
twelve

You may use whatever programming language you wish.
'''
a = ["five","twenty six","nine hundred ninety nine","twelve","eighteen",
     "one hundred one","fifty two","forty one","seventy seven",
     "six","twelve","four","sixteen"]

b = {"five": 5,"twenty six": 26, "nine hundred ninety nine": 999,
     "twelve": 12,"eighteen": 18,"one hundred one": 101,"fifty two": 52,
     "forty one": 41,"seventy seven": 77, "six": 6,"twelve": 12,
     "four": 4,"sixteen": 16}

for i in a:
  for key, value in b.items():
    if key == i and value % 3 == 0:
      print(key)