class shape():
    def shapearea(self,l,w,h):
        self.l=l
        self.w=w
        self.h=h
        print("Length:",self.l)
        print("Width:",self.w)
        print("Height:",self.h)        

class square(shape):
    def squarearea(self):
        print("square area=2*l:",2*self.l)

class rectangle(shape):
    def rectanglearea(self):
        print("rectangle area=l*w:",self.l*self.w)

class box(square,rectangle):
    def boxarea(self):
        print("box area=l*w*h:",self.l*self.w*self.h)

b1=box()
l=int(input("Enter L:"))
w=int(input("Enter W:"))
h=int(input("Enter H:"))
b1.shapearea(l,w,h)
b1.squarearea()
b1.rectanglearea()
b1.boxarea()

    
