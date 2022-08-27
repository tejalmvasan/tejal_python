'''
Write a Python program to add 'ing' at the end of a given string (length
should be at least 3). If the given string already ends with 'ing' then add 'ly'
insteadif the string length of the given string is less than 3, leave it
unchanged

s1=ab
o/p = ab

s1= abc
o/p= abcing

s=string
o/p= stringly
o/p = strly

'''

s = input("enter the string : ")
if len(s) < 3:
  print(s)
elif s[-3:] == 'ing':
  print("With ing : ", s + 'ly')
  print("without ing : ", s[:-3] + 'ly')
else:
  print(s + 'ing')
  

    
