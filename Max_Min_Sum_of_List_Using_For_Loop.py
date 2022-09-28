'''
without function minimum, maximum and sum of list element
'''

list = []
num = int(input('How many elements to put in List: '))
for n in range(num):
    element = int(input('Enter element: '))
    list.append(element)
print("Minimum element in the list is :", min(list))
print("Maximum element in the list is :", max(list))
print("sum of elements in the list is :", sum(list))
