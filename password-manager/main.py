from tkinter import *
from tkinter import ttk, messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    letters_list = [random.choice(letters) for n in range(nr_letters)]
    #
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    numbers_list = [random.choice(numbers) for n in range(nr_numbers)]
    #
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)
    symbols_list = [random.choice(symbols) for n in range(nr_symbols)]

    password_list = letters_list + numbers_list + symbols_list

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char
    password = "".join(password_list)
    pyperclip.copy(password)
    password_input.delete(0, END)
    password_input.insert(0, password)

    # print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    username = username_input.get()
    website = website_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(message="Please do not leave empty fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nUsername: {username}\nPassword: {password}\n Is it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)

            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)


            else:
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)


def search():

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            selection = data[website_input.get()]
            username = selection["username"]
            password = selection["password"]
            # angela's solution
            # website = website_input.get()
            # if website in data:
            #     username = data[website]["username"]
            #     password = data[website]["password"]
            # else:
            #     messagebox.showinfo(title="Error", message="There is no entry for that website")

    except FileNotFoundError:
        messagebox.showinfo(message="There is no data file")

    except KeyError:
        messagebox.showinfo(title="Error", message="There is no entry for that website")

    else:
        messagebox.showinfo(message=f"Username: {username}\n Password: {password}")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password manager")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.gif")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry(width=25)
website_input.grid(column=1, row=1)
website_input.focus()

search_button = ttk.Button(text="Search", command=search)
search_button.grid(column=2, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

username_input = Entry(width=35)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0, "paolo.dizon@me.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = Entry(width=20)
password_input.grid(column=1, row=3)

generate_button = ttk.Button(text="Generate Password", command=gen_pass)
generate_button.grid(column=2, row=3)

add_button = ttk.Button(text="Add", width=32, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()