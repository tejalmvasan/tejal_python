'''
Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string.
s1= tejal
s2= vasan
o/p = vajal tesan
'''

s1 = input ( "Please Enter First String : " )
s2 = input ( "Please Enter Second String : " )

# swap
x = s2[: 2 ] + s1[ 2 :]
y = s1[: 2 ] + s2[ 2 :]

print ( "Your first has become :- " ,x,y)

