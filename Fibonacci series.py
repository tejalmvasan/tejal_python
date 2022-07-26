'''
Write a Python program to get the Fibonacci series of given range.
serias = 0 1 1 2 3 5 8 13
0 1 addition 0+1=1 
add last to 1+1 =2
'''

n=int(input("Enter N:"))
a,b=0,1
while b<n:
    print(b,end=" ")
    a,b=b,a+b
