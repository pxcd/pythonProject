import tkinter
import random
import time

window = tkinter.Tk()
window.title("IP Tracer")
window.minsize(width=300, height=300)
window.config(padx=100, pady=100)


def generate_ip():
    new_text = (f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}")
    time.sleep(2)
    result.config(text=new_text)


title_label = tkinter.Label(text="GUI interface using Visual Basic to track the killer's IP address", font=("Helvetica", 24))
title_label.grid(column=3, row=1)



button = tkinter.Button(text="Trace IP Address", command=generate_ip)
button.grid(column=3, row=4)



result = tkinter.Label(text="0.0.0.0", font=("Helvetica", 18))
result.grid(column=3, row=2)



window.mainloop()
