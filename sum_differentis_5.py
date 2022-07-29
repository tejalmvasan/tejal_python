'''
Write a Python program that will return true if the two given integer values
are equal or their sum or difference is 5.

'''

# 5,5 = true
# 1+4 =5 true
# 10-5 =5 true

x=int(input("Enter X:"))
y=int(input("Enter Y:"))

if x==y or x-y==5 or x+y==5:
    print("true")
else:
    print("False")
