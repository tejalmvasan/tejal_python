import random

data=open("data.txt","w")
for i in range(10):
    data.write(str(random.randint(1,100))+",")
data.close()

data=open("data.txt","r")
odd=open("odd.txt","w")
even=open("even.txt","w")

l=data.read().split(",")[:-1]

for i in l:
    if int(i)%2==0:
        even.write(i+",")
    else:
        odd.write(i+",")

data.close()
odd.close()
even.close()

print("Data File Content")
data=open("data.txt","r")
print(data.read())
data.close()

print("Even File Content")
even=open("even.txt","r")
print(even.read())
even.close()

print("Odd File Content")
odd=open("Odd.txt","r")
print(odd.read())
odd.close()


