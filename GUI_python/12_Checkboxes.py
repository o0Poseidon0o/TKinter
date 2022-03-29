

from tkinter import *
from PIL import ImageTk,Image #Phai cai Pillow. pip install pillow

root = Tk()
root.title("Check box")
root.iconbitmap("image/icon.ico")
root.geometry("400x400") # mac dinh mo chuong trinh co kich thuoc 400 x 400

def show():
    myLable = Label(root, text=var.get()).pack()

var= StringVar()

c=Checkbutton(root, text="Hay chon o day!!!", variable=var, onvalue="on", offvalue="off")
c.deselect()
c.pack()



mybutton=Button(root, text="Show selection", command=show).pack()


root.mainloop()