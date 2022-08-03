from tkinter import *
from random import choice, randint, shuffle
from tkinter import messagebox
import pyperclip


# PASSWORD GENERATOR
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_in_password = [choice(letters) for i in range(randint(8, 10))]
    numbers_in_password = [choice(numbers) for i in range(randint(2, 4))]
    symbols_in_password = [choice(symbols) for i in range(randint(2, 4))]

    password_list = letters_in_password + numbers_in_password + symbols_in_password
    shuffle(password_list)

    # to convert list to string
    final_password = "".join(password_list)
    password_entry.insert(0, final_password)
    pyperclip.copy(final_password)


# SAVE PASSWORD
def add_password():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oopps", message="Please don't leave any field empty")

    else:
        message = f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it okay to save it?"
        is_ok = messagebox.askokcancel(title=website, message=message)

        if is_ok:
            with open("data.txt", mode="a") as data:
                data.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# UI SETUP
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:", bg="white")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3)

# Entry
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "example@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=40, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
