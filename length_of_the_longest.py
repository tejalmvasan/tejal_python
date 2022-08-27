'''
Write a Python function that takes a list of words and returns the length
of the longest one.
'''

def list_long(list):
   max = len(list[0])
   temp = list[0]

   for i in list:
      if(len(i) > max):
         max = len(i)
         temp = i
   return max

list = ["tejal", "hardik", "Bhagwati", "kiran"]
print("The list is :",(list))
print("The result is :",list_long(list))


