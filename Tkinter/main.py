from struct import pack
from tkinter import *
from tkinter.ttk import *


window = Tk()

window.title("GUI")
window.geometry("700x500")


# txt = Entry(window, width= 20)
# txt.grid(column=0, row = 0)

# def click():
#     grt = f"How are you doing today ,{txt.get()}"
#     l1 = Label(window, bg="ivory", fg="darkgreen")
#     l1.grid(column=0,row=2)
#     l1.config(text= grt)

# # label = tkinter.Label(window, text = "Hello, world").pack()

# # l1 = Label(window, text = "Tesla", font=("Monospace", 50))
# # l1.grid(column=15,row=15)

# bt = Button(window, text = "Submit", command= click)
# bt.grid(column=1, row= 0)





combo = Combobox(window)
combo['values'] = (1,2,3,4,5, "Text")
combo.current(3)
combo.grid(column = 20, row= 20)

chk_btn = BooleanVar()
chk_btn.set (True)
btn = Checkbutton(window, text = "Select", var = chk_btn)
btn.grid(column = 20, row =10)
window.mainloop()