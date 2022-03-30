#phai cai "pip install numpy"
#pip install matplotlib

from tkinter import *
import numpy as np
import matplotlib.pyplot as plt


root = Tk()
root.title("Ve bieu do")

def graph():
    gianha=np.random.normal(200000,25000,5000)
    plt.hist(gianha)
    plt.show()



my_button=Button(root, text="Graph It!", command=graph)
my_button.pack()


root.mainloop()
