class student: #class create
    #function create
    def getdata(self,fname,lname):
        self.f=fname
        self.l=lname

    def putdata(self):
        print("First Name: ",self.f)
        print("Last Name: ",self.l)

s1=student() #object create s1
s2=student()

s1.getdata("Tejal", "Vasan") #function call(with argument)
s1.putdata()
    
