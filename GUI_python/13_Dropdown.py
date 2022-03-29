from tkinter import *
from PIL import ImageTk,Image #Phai cai Pillow. pip install pillow

root = Tk()
root.title("Dropdown box")
root.iconbitmap("image/icon.ico")
root.geometry("400x400") # mac dinh mo chuong trinh co kich thuoc 400 x 400


def show():
    myLabel= Label(root, text=clicked.get()).pack()

options=[
    "Thu hai",
    "Thu ba",
    "Thu tu",
    "Thu nam",
    "Thu sau",
]

clicked = StringVar()
clicked.set(options[0]) # Mac dinh gia tri la Thu hai

drop = OptionMenu(root, clicked, *options) #Dau * de truoc list thi se chon tung gia tri
drop.pack()

mybutton= Button(root, text="show selection", command=show).pack()

root.mainloop()