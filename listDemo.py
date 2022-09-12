l=[23,25,10,1.3]
print("List of L:",l)

l.append(12) # Adds an element at the end of the list
print ("Append in L:",l)

l.clear() #Removes all the elements from the list
print("Clear List is:",l)

l1=[23,25,10,1.3,21,1,3,6,1,1,1,1]
print("List of L1:",l1)

l2=l1.copy()#Returns a copy of the list
print("L1 is copy into L2 : ",l2)

#Returns the number of elements with the specified value
print ("count of 1 in list L1: ",l1.count(1))

#Add elements to the end of the current list
l3=[1000,2000]
l4=[100,200,300,400]

l3.extend(l4)
print("L3 list is: ",l3)
print("L4 list is:",l4)

#Returns the index of the first element with the specified value
l=[23,25,10,1.3]
print("List of L:",l)
print("Index is :",l.index(1.3))

#Adds an element at the specified position
l.insert(0,63.63)
print("after insert element:",l)

#Removes the last element
l.pop() 
print("After pop the item in list:",l)

#Removes the element at the specified position
l4.pop(2)
print("After pop the item in list 4 :",l4)

#Removes the first item with the specified value
l4.remove(200)
print("After remove element:",l4)

#Reverses the order of the list
l3.reverse()
print("ater reverse:",l3)

#Sorts the list
l3.sort()
print("After Sort:",l3)

