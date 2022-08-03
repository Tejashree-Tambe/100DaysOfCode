from tkinter import *
from random import choice, randint, shuffle
from tkinter import messagebox
import pyperclip
import json


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
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oopps", message="Please don't leave any field empty")

    else:
        message = f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it okay to save it?"
        is_ok = messagebox.askokcancel(title=website, message=message)

        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)                 # Reading old data

            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                data.update(new_data)                           # updating new data

                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)        # saving updated data

            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# SEARCH CREDENTIALS
def search_credentials():
    website = website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            all_websites = json.load(data_file)

            try:
                website_email = all_websites[website]["email"]
                website_password = all_websites[website]["password"]

            except KeyError:
                messagebox.showinfo(title=website, message="No such website database exists")


            else:
                message = f"Email:{website_email} \nPassword:{website_password}"
                messagebox.showinfo(title=website, message=message)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File exists")


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
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "example@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons
search_button = Button(text="Search", command=search_credentials)
search_button.grid(column=2, row=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=40, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
