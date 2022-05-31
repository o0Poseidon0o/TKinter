import random
from time import sleep
from turtle import update
def generate_number():
    #list = ["1","2","3"]
    #number = ""
    #for i in range(1):
        #number = number + random.choice(list)
    #l2.config(text= number)
    value =random.randint(1,200)
    l2.config(text=value)
    sleep(5)
    print("CHUC MUNG BAN DA CHIEN THANG!!!!!")
 
import tkinter as tk
window = tk.Tk()
window.geometry("900x900")
window.config(bg="#F39C12")
window.resizable(width=False,height=False)
window.title('QUAY SO NGAU NHIEN') 
 
l1 = tk.Label(text="QUAY SO NGAU NHIEN",font=("Arial",20),bg="Black",fg="White")

b1 = tk.Button(text="BAT DAU",font=("Arial",15),bg="#A3E4D7",command=generate_number)

l2 = tk.Label(bg="#F39C12",font=("Arial",50),text="0")

l1.place(x=100,y=20)
b1.place(x=110,y=70)
l2.place(x=165,y=130)
window.mainloop()