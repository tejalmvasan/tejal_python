from _collections import deque
l=deque([])
l.append(10)
print(list(l))
l.append(20)
print(list(l))
l.append(30)
print(list(l))
l.append(40)
print(list(l))
l.append(50)
print(list(l))
l.popleft() #10
print(list(l))
l.popleft() #20
print(list(l))
l.popleft() #30
print(list(l))
l.popleft() #40
print(list(l))
l.popleft() #50
print(list(l))

