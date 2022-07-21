d={1:"Dharma",2:"Khushali",3:"Tejal",4:"Mohit",5:"Nikunj"}

print(d)
print(d[2])
print(d.get(3))
print(d.items())
print(d.keys())
print(d.pop(1))
print(d)
print(d.popitem())
print(d)
d1={10:"Dharma",20:"Nikunj"}
d.update(d1)
print(d)
print(d.values())

for i in d:
    print(i," : ",d[i])
    
d[10]="Jigar"

print(d)
