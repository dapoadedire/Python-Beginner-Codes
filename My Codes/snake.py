import random
import tkinter as tk
from PIL import Image,ImageTk


window=tk.Tk()
window.geometry("500x700")
window.title("twitter.com/dapo_adedire")


def write():
    a("a b c")
text_area=tk.Text(master=window,height=25,width=33, bg="blue")
text_area.grid(column=15,row=2)
content = "{a}".format(a= a, font = ('arial', 12,'bold')) 
text_area.insert(tk.END, content)


button1=tk.Button(text="   Button 🔳   ",bg="red", height=1,width=12,font=('arial',15,'bold'))
button1.grid(column=15,row=1)

window.mainloop()