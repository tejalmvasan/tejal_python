def printline():
    print("*"*20)
printline()

def pattern(n):
    for i in range (1,n+1):
        print("*"*i)

def oddeven(a):
    if a%2==0:
        print("Number is Even",a)
    else:
        print("Number is Odd",a)

def maxoftwo(a,b):
    if a>b:
        print("A is greater",a)
    else:
        print("B is greater",b)

def maxofthree(a,b,c):
    if a>b:
        if a>c:
            print("A is greater Number",a)
        else:
            print("C is greater Number",c)
    elif b>c:
        print("B is greater Number",b)
    else:
            print("C is greater Number",c)
while True:
    print("1.Pattern")
    print("2.oddeven")
    print("3.maxoftwo")
    print("4.maxofthree")
    print("5.exit")

    c=int(input("Enter your Choice: "))
    if c==1:
        n=int(input("Enter N: "))
        pattern(n)
        printline()
    elif c==2:
        m=int(input("Enter M: "))
        oddeven(m)
        printline()
    elif c==3:
        a=int(input("Enter A: "))
        b=int(input("Enter B: "))
        maxoftwo(a,b)
        printline()
    elif c==4:
        x=int(input("Enter X: "))
        y=int(input("Enter Y: "))
        z=int(input("Enter Z: "))
        maxofthree(x,y,z)
        printline()
    elif c==5:
        print("You are exit on loop")
        break
    else:
        print("Invalid Choice")
        printline()





