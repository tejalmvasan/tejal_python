'''
Write a python function to insert a string in the middle of a string.
'''

def insert_middle(str1,word):
    pos = int(len(str1)/2)
    mid = str1[:pos] + word + str1[pos:]
    return mid
str1=input("Enter your string:")
print(len(str1))
word=input("Enter your middle:")
print(insert_middle(str1,word))


   
