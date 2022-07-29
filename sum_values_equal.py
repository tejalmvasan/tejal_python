'''
Write a Python program to sum of three given integers.However, if two
values are equal sum will be zero.
'''


a=int(input("Enter A:"))
b=int(input("Enter B:"))
c=int(input("Enter C:"))

if a == b or b == c or c == a:
    sum = 0
else:
    sum = a + b + c
print("Sum is :",sum)
