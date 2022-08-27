class A:
    def show(self):
        print("Show from A")

class B(A):
    def show(self):
        super().show()
        print("show from B")

class C(B):
    def show(self):
        super().show()        
        print("show from C")

c1=C()
c1.show()
        
