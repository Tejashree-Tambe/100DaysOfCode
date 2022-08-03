from tkinter import *

MILES_TO_KM = 1.6


def convert():
    miles_value_input = int(miles_value.get())
    km_output = miles_value_input * MILES_TO_KM
    km_value.config(text=int(km_output))


window = Tk()
window.title("Convert miles to km")
window.minsize(width=360, height=200)
window.config(padx=20, pady=30)

is_equal_to = Label(text="is equal to", padx=40, pady=30)
is_equal_to.grid(column=0, row=1)

km_value = Label(text="0")
km_value.grid(column=1, row=1)

miles_value = Entry(width=10)
miles_value.grid(column=1, row=0)

km = Label(text="Km")
km.grid(column=2, row=1)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

calculate = Button(text="Calculate", command=convert)
calculate.grid(column=1, row=2)

window.mainloop()
