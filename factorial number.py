'''
factorial number of given number
fac
1*2*3=6
'''

n=int (input ("Enter N: "))
fac =1
while (n>0):
    fac=fac*n
    n=n-1
print("Factorial = ",fac)
