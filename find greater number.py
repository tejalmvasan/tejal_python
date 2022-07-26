'''
find greater number
'''

a=int(input("Enter Number A:"))
b=int(input("Enter Number B:"))
c=int(input("Enter Number C:"))

if a>b: 
    if a>c: 
        print("A is Greater Number")
    else:
        print("C is Greater Number")
elif b>c:
    print("B is Greater Number")
else:
    print("C is Greater Number")
    
