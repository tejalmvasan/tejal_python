def printline():
    print("*"*20)
printline()

print("1.Pattern Function")
printline()
def pattern(n):
    for i in range (1,n+1):
        print("*"*i)
pattern(5)
printline()

print("2.oddeven Function")
printline()
def oddeven(a):
    if a%2==0:
        print("Number is Even",a)
    else:
        print("Number is Odd",a)
x=int(input("Enter X:"))
oddeven(x)
printline()

print("3.maxoftwo Function")
printline()
def maxoftwo(a,b):
    if a>b:
        print("A is greater",a)
    else:
        print("B is greater",b)
x=int(input("Enter Value A:"))
y=int(input("Enter Value B:"))
maxoftwo(x,y)

printline()
print("4.maxofthree Function")
printline()
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
x=int(input("Enter Value A:"))
y=int(input("Enter Value B:"))
z=int(input("Enter Value C:"))
maxofthree(x,y,z)






