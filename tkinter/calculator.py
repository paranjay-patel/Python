from tkinter import *
from unittest import result 

window = Tk()
window.title("mile to kilometer converter")
window.config(padx=20, pady=20)

input = Entry(width=15)
input.grid(column = 1,row = 0)
print(input.get())

eq = Label(text="is equal to",font=("Arial",15,"bold"))
eq.grid(column = 0, row = 1)

miles = Label(text="miles",font=("Arial",15,"bold"))
miles.grid(column = 2, row = 0)

km = Label(text="km",font=("Arial",15,"bold"))
km.grid(column = 2, row = 1)

answer = Label(text="0",font=("Arial",15,"bold"))
answer.grid(column = 1, row = 1)


def button_clicked():
    print("I got clicked")
    new_text = float(input.get())
    answer.config(text=round(new_text*1.609,1))

button = Button(text="calculate",command=button_clicked)
button.grid(column=1,row=2)




window.mainloop()