'''
Write a Python function to reverses a string if its length is a multiple of 4.
'''
def reverse(str1):
    if len(str1)% 4 == 0:
        return (str1[::-1])
    else:
        return str1
str1 = input("Enter a string:")
print("The given string is:", str1)
print("Reversed string is:", reverse(str1))
