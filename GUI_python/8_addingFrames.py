
from tkinter import *

from PIL import ImageTk,Image #Phai cai Pillow. pip install pillow

root = Tk()
root.title("Test thoat chuong trinh")
frame= LabelFrame(root, text='This is my Frame...', padx=50,pady=50) #padx vi tri xuat hien 
frame.pack(padx=10, pady= 10)

b=Button(frame, text="Don't Click here")
b2=Button(frame, text="Don't Click here")
#b.pack()
b.grid(row=0,column=1)
b2.grid(row= 1,column=2)


root.mainloop()