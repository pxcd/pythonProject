import tkinter

window = tkinter.Tk()
window.title("Mile to KM Converter")
window.minsize(width=300, height=300)
window.config(padx=100, pady=100)


def convert():
    new_text = input.get()
    int_input = round(int(new_text) * 1.609)
    result_label.config(text=int_input)


miles_label = tkinter.Label(text="Miles", font=("Helvetica", 18))
miles_label.grid(column=4, row=1)

is_equal_to_label = tkinter.Label(text="is equal to", font=("Helvetica", 18))
is_equal_to_label.grid(column=2, row=2)

button = tkinter.Button(text="Calculate", command=convert)
button.grid(column=3, row=4)

input = tkinter.Entry(width=10)
input.grid(column=3, row=1)

result_label = tkinter.Label(text="0", font=("Helvetica", 18))
result_label.grid(column=3, row=2)

km_label = tkinter.Label(text="Km", font=("Helvetica", 18))
km_label.grid(column=4, row=2)

window.mainloop()
