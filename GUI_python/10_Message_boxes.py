
from tkinter import *
from tkinter import messagebox



from PIL import ImageTk,Image #Phai cai Pillow. pip install pillow

root = Tk()
root.title("Test thoat chuong trinh")

#showinfo ,showwarning, showerror, askokcancel, askquestion, askyesno, askretrycancel

def popup():
    a = messagebox.showinfo("This is my Popup", "Hello World!")
    Label(root, text=a).pack() #Kiem tra gia tri cua messagebox la gi
    #if responses == "yes":
        #Label(root, text= "You clicked Yes!").pack()
    #else:
        #Label(root, text= "You click No!!").pack()


Button(root, text="Popup", command=popup).pack() 


root.mainloop()