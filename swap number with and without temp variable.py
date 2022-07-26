'''
Write python program that swap two number with temp variable and
without temp variable.
'''

print("with temp")
x=int(input("ENTER X:"))
y=int(input("ENTER Y:"))

temp=x
x=y 
y=temp 
print("X after swap:",x)
print("Y after swap:",y)

print("without temp")
x=int(input("ENTER X:"))
y=int(input("ENTER Y:"))

x,y=y,x
print("X after swap:",x)
print("Y after swap:",y)
