import random
data1=open("data12.txt","w")

for i in  range(10):
    data1.write(str(random.randint(1,100))+",")
data1.close()

data1=open("data12.txt","r")
print(data1.read())
data1.close()
