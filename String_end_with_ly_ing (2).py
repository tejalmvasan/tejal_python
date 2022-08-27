'''
s1=ab
o/p = ab

s1= abc
o/p= abcing

s=string -- ing replace with ly
o/p= strly
'''


s = input("enter the string : ")
if len(s) < 3:
  print(s)
elif s[-3:] == 'ing':
  print(s[:-3] + 'ly')
else:
  print(s + 'ing')

