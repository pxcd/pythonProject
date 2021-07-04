from tkinter import *
from tkinter import Tk
from pandas import *
import random


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# to_learn can either be 1) original data, if new data does not exist when FileNotFoundError
# or 2) new data (default)
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
# to_learn is a list

def next_card():
    # set current_card to global because flip() will use it
    global current_card
    current_card = random.choice(to_learn)
    print(current_card)
    canvas.itemconfig(canvas_img, image=front_img)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    window.after(3000, flip)


def flip():
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_img, image=back_img)
    canvas.itemconfig(title_text, text="English", fill="white")
    window.after_cancel(NONE)


def is_known():
    # remove the current_card (dictionary) from to_learn (list).
    # if ran for the first time, original_data is read
    # for succeeding runs, new data is read
    to_learn.remove(current_card)
    # initialize data as dataframe
    data = pandas.DataFrame(to_learn)
    # if ran for the first time, original_data (from french_words.csv) is read and
    # written to a new csv file. for succeeding runs, new data (words_to_learn.csv)
    # is ALWAYS read and trimmed until it's empty / when you know all the french words
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.gif")
canvas_img = canvas.create_image(400, 263, image=front_img)
title_text = canvas.create_text(400, 150, text="Title", fill="black", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", fill="black", font=("Arial", 60, "bold"))
back_img = PhotoImage(file="images/card_back.gif")
canvas.grid(column=1, row=1, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.gif")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=1, row=2)


right_img = PhotoImage(file="images/right.gif")
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(column=2, row=2)


next_card()











window.mainloop()