
from email.mime import image
from tkinter import *
from PIL import ImageTk,Image #Phai cai Pillow. pip install pillow

root = Tk()
root.title("Test thoat chuong trinh")

top = Toplevel()
my_img= ImageTk.PhotoImage(Image.open("image/doreamon.png"))
my_label = Label(top,image=my_img).pack()


root.mainloop()