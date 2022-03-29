
from email.mime import image
from tkinter import *
from PIL import ImageTk,Image #Phai cai Pillow. pip install pillow

root = Tk()
root.title("Test thoat chuong trinh")
root.iconbitmap("image/icon.ico")

def open():
    global my_img
    top = Toplevel()
    top.title("Cua so khac")
    my_img= ImageTk.PhotoImage(Image.open("image/doreamon.png"))
    my_label = Label(top,image=my_img).pack()
    btn2=Button(top, text="close windows", command=top.destroy).pack()


btn=Button(root, text="Open second windows",command=open).pack()



root.mainloop()