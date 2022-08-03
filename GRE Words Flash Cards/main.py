from tkinter import *
import json

BACKGROUND_COLOR = "#B1DDC6"
TIMER_FONT = ("Courier", 30, "bold")
TITLE_FONT = ("Courier", 33, "italic")
CONTENT_FONT = ("Courier", 35, "bold")
CURRENT_INDEX = 0
ALL_WORDS = []
to_learn = {}
timer = None


try:
    with open("data/to_learn.json", "r") as data_file:
        data = json.load(data_file)

except FileNotFoundError:
    with open("data/baron-334.json") as data_file:
        original_data = json.load(data_file)
        to_learn = original_data

else:
    to_learn = data


def user_knows():
    global to_learn
    del to_learn["words"][CURRENT_INDEX]

    with open("data/to_learn.json", "w") as to_learn_file:
        json.dump(to_learn, to_learn_file, indent=4)

    show_next_card()


def show_back_card():
    card.itemconfig(card_background, image=back_card_img)
    card.itemconfig(card_title, text="Meaning")

    meaning = to_learn["words"][CURRENT_INDEX]["definition"]
    card.itemconfig(card_content, text=meaning, width=700)


def show_next_card():
    global CURRENT_INDEX, flip_timer
    CURRENT_INDEX += 1
    word = to_learn["words"][CURRENT_INDEX]["word"]

    window.after_cancel(flip_timer)

    card.itemconfig(card_background, image=front_card_img)
    card.itemconfig(card_content, text=word)

    flip_timer = window.after(3000, func=show_back_card)


#  UI
window = Tk()
window.title("TOEFL Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=show_back_card)

card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file="images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")
card_background = card.create_image(400, 263, image=front_card_img)
card_title = card.create_text(400, 103, text="Word", font=TITLE_FONT)
card_content = card.create_text(400, 263, text="Word", font=CONTENT_FONT)
card.grid(column=1, row=0, columnspan=2)

wrng_button_img = PhotoImage(file="images/wrong.png")
wrng_button = Button(highlightthickness=0, image=wrng_button_img, command=show_next_card)
wrng_button.grid(column=1, row=2)

right_button_img = PhotoImage(file="images/right.png")
right_button = Button(highlightthickness=0, image=right_button_img, command=user_knows)
right_button.grid(column=2, row=2)

show_next_card()

window.mainloop()
