import tkinter

window = tkinter.Tk()
window.title("My First GUI Interface lol")
window.minsize(width=500, height=300)


def button_click():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


#Label
my_label = tkinter.Label(text="I am a label", font=("Helvetica", 24, "bold"))
my_label.config(text="New Text2")
# my_label.pack(side="left")
# my_label.place(x=100, y=200)
my_label.grid(column=1, row=1)
# my_label["text"] = "New Text"
# or
my_label.config(padx=50, pady=50)




#BUTTONS
button = tkinter.Button(text="click me", command=button_click)
# button.pack()
button.grid(column=2, row=2)

# Entry

input = tkinter.Entry(width=10)
print(input.get)
input.grid(column=3, row=3)
# input.pack()





# put at the very end
window.mainloop()
