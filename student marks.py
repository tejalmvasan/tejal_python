rno=int(input("Enter Roll No: "))
sname=input("Enter Student Name: ")

s1=int(input("Enter Marks of subject 1: "))
s2=int(input("Enter Marks of Subject 2: "))
s3=int(input("Enter Marks of Subject 3: "))

total = s1+s2+s3
per=((total*100)/300)

print("Roll No: ",rno)
print("Student Name: ",sname)
print("TotalMarks of Subject: ",total)
print("Percentage: ",per)

if per>=70:
    print("Distriction")
elif per>=60:
    print("First Class")
elif per>=50:
    print("Second Class")
elif per>=40:
    print("Pass Class")
else:
    print("Fail")
