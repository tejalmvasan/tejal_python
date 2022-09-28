'''
Write a Python program to remove duplicates from a list.
'''

a=[10,20,10,20,30,40]
dup_items=set()
uniq_items=[]
for i in a:
    if i not in dup_items:
        uniq_items.append(i)
        dup_items.add(i)
print("List of Items:",a)
print("Aftre remove Duplicate item:",dup_items)
print("Uniq item:",uniq_items)        
