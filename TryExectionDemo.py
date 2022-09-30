print("Star Code")
try:
    
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a/b
    print("Division : ",c)
    
except Exception as e:
    print("Exception Caught",e)

print("End Code")


'''
except ZeroDivisionError as e:
    print("Exception Caught",e)
except ValueError as e:
    print("Exception Caught",e)
'''
