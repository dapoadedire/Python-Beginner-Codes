import tkinter as tk
from tkinter import *
import randfacts
import time
# function to add facts
def move():
    facts = randfacts.getFact(False)
    c = "*)"
    label = Label(root, text=c+facts)
    label.pack()
   
  
def destroy():
    root.destroy()
   
  
root = tk.Tk()
# adjust window
root.config(bg="red")
root.geometry("400x40")
  
# add buttons
button = tk.Button(root, text="Click here for Facts", command=move)
button2 = tk.Button(root, text="Clear and quit", command=destroy)
button.pack()
button2.pack()
  
root.mainloop()