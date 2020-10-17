"""
Print out all of the strings in the following array in alphabetical order 
sorted by the middle letter of each string, each on a separate line. 
If the word has an even number of letters, choose the later letter, 
i.e. the one closer to the end of the string.

['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 
'Samba', 'Rumba', 'Paso Doble', 'Jive']

The expected output is:
'Cha Cha'
'Paso Doble'
'Viennese Waltz'
'Waltz'
'Samba'
'Rumba'
'Tango'
'Foxtrot'
'Jive'

You may use whatever programming language you'd like.
"""

a = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 
     'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']
     
def print_sorted(words):
  cache = {}
  for w in words:
    letter = w[(len(w)//2)]

    if letter not in cache:
      cache[letter] = [w]
    else:
      cache[letter].append(w)

  for dance in sorted(list(cache.keys())):
    for d in range(len(cache[dance])):
      print (cache[dance][d])

print_sorted(a)