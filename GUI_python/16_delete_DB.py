from tkinter import *
from webbrowser import get
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
'''
c.execute("""CREATE TABLE addresses 
                (first_name text,
                last_name text,
                address text,
                city text,
                state text,
                zipcode integer)
""")
'''
def delete():
     #Tao database hoac ketnoi 1 database
    conn=sqlite3.connect('address_book.db')
    #Tao cursor (con tro)
    c=conn.cursor()

    #Delete a record
    c.execute("DELETE from addresses WHERE oid= " + delete_box.get())

    #commit change
    conn.commit()
    #dong ket noi
    conn.close()

# Tao submit 
def  submit():
    #Tao database hoac ketnoi 1 database
    conn=sqlite3.connect('address_book.db')
    #Tao cursor (con tro)
    c=conn.cursor()
    #Insert Into Table
    c.execute ("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
            {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'address': address.get(),
                'city': city.get(),
                'state': state.get(),
                'zipcode': zipcode.get()           
            })

    #commit change
    conn.commit()
    #dong ket noi
    conn.close()

    #Xoa text boxes
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)

#Tao Query function
def query():
     #Tao database hoac ketnoi 1 database
    conn=sqlite3.connect('address_book.db')
    #Tao cursor (con tro)
    c=conn.cursor()
    #Insert Into Table
    c.execute ("SELECT *, oid FROM addresses")
    records=c.fetchall()
    print(records)
    #Loop Thru Results
    print_records=''
    for record in records:
        print_records += str(record[0]) + " " +str(record[1])+"\t"+ str(record[6]) +"\n"

    query_label = Label(root, text= print_records)
    query_label.grid(row=8, column=0, columnspan=2)


    #commit change
    conn.commit()
    #dong ket noi
    conn.close()

# Tao Text boxes
f_name= Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)
l_name= Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
address= Entry(root, width=30)
address.grid(row=2, column=1, padx=20)
city= Entry(root, width=30)
city.grid(row=3, column=1, padx=20)
state= Entry(root, width=30)
state.grid(row=4, column=1, padx=20)
zipcode= Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1)

#Tao text boxes Labels
f_name_label=Label(root,text="First name")
f_name_label.grid(row=0,column=0)
l_name_label=Label(root,text="Last name")
l_name_label.grid(row=1,column=0)
address_label=Label(root,text="address")
address_label.grid(row=2,column=0)
city_label=Label(root,text="City")
city_label.grid(row=3,column=0)
state_label=Label(root,text="state")
state_label.grid(row=4,column=0)
zipcode_label=Label(root,text="zipcode")
zipcode_label.grid(row=5,column=0)

delete_box_label=Label(root, text="ID number")
delete_box_label.grid(row=9,column=0)

# Tao submit button
submit_btn=Button(root, text="Add record to Database",command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=20, padx=20, ipadx=100)
# Tao Query Button
query_btn= Button(root, text="show records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=137 )
#Tao delete button
delete_btn= Button(root, text="Delete records", command=delete)
delete_btn.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=137 )


#commit change
conn.commit()
#dong ket noi
conn.close()

root.mainloop()