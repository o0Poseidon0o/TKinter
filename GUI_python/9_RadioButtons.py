from tkinter import *


from PIL import ImageTk,Image #Phai cai Pillow. pip install pillow

root = Tk()
root.title("Test thoat chuong trinh")

#r=IntVar() #Ep kieu sang kieu Int
#r.set("2")

Tuples =[
    ("a","1"),
    ("b","2"),
    ("c","3"),
    ("d","4"),
]

dapan= StringVar()
dapan.set("")

for  text,tuples in Tuples:
    Radiobutton(root, text=text, variable=dapan, value= tuples).pack(anchor=W)

def clicked(value):
    mylabel = Label(root, text=value)
    mylabel.pack()

#Radiobutton(root, text='Lua chon 1', variable= r, value=1, command=lambda:clicked(r.get())).pack()
#Radiobutton(root, text='Lua chon 2', variable= r, value=2,command=lambda:clicked(r.get())).pack()

mylabel = Label(root, text=dapan.get())
mylabel.pack()

myButton = Button(root, text="Click me!", command=lambda:clicked(dapan.get()))
myButton.pack()


root.mainloop()