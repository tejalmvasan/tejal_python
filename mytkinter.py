from tkinter import *

root=Tk()
root.title("my first program")
root.geometry("360x420")
root.resizable(width=False,height=False)

l_id=Label(root,text="FORM",fg="Black",font=("Algerian",12))
l_id.place(x=150,y=10)

l_id=Label(root,text="ID NO.")
l_id.place(x=50,y=50)

l_fname=Label(root,text="FIRST NAME")
l_fname.place(x=50,y=100)

l_lname=Label(root,text="LAST NAME")
l_lname.place(x=50,y=150)

l_email=Label(root,text="EMAIL")
l_email.place(x=50,y=200)

l_mobile=Label(root,text="MOBILE")
l_mobile.place(x=50,y=250)

e_id=Entry(root)
e_id.place(x=150,y=50)

e_fname=Entry(root)
e_fname.place(x=150,y=100)

e_lname=Entry(root)
e_lname.place(x=150,y=150)

e_email=Entry(root)
e_email.place(x=150,y=200)

e_mobile=Entry(root)
e_mobile.place(x=150,y=250)

insert=Button(root,text="INSERT",bg="black",fg="white",font=("Impact",12))
insert.place(x=50,y=300)

search=Button(root,text="SEARCH",bg="black",fg="white",font=("Impact",12))
search.place(x=115,y=300)

update=Button(root,text="UPDATE",bg="black",fg="white",font=("Impact",12))
update.place(x=184,y=300)

delete=Button(root,text="DELETE",bg="black",fg="white",font=("Impact",12))
delete.place(x=250,y=300)






















