from tkinter import *
from PIL import ImageTk,Image #Phai cai Pillow. pip install pillow
import sqlite3

root = Tk()
root.title("DATABASE")
root.iconbitmap("image/icon.ico")
root.geometry("400x400") # mac dinh mo chuong trinh co kich thuoc 400 x 400

#Tao database hoac ketnoi 1 database
conn=sqlite3.connect('address_book.db')
#Tao cursor (con tro)
c=conn.cursor()
#Tao bang
c.execute("""CREATE TABLE addresses 
                (first_name text,
                last_name text,
                address text,
                city text,
                state text,
                zipcode integer)
""")

#commit change
conn.commit()
#dong ket noi
conn.close()


root.mainloop()