'''
Write a Python program to find whether a given number is even or odd,
print out an appropriate message to the user.

'''

n=int(input("Enter Number N:"))
for i in range(1,n+1):
    if i%2==0:
        print(i, "Is Even Number")
    else:
        print(i, "Is Odd Number")
print("Your Program is Right")
