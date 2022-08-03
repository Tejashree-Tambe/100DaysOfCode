import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("GUI Tkinter")
window.minsize(width=500, height=300)

my_label = Label(text="label")
my_label.grid(column=0, row=0)

button1 = Button(text="button1")
button1.grid(column=1, row=1)

button2 = Button(text="button2")
button2.grid(column=2, row=0)

entry = Entry()
entry.grid(column=3, row=3)

window.mainloop()
