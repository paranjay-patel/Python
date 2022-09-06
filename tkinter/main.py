from tkinter import * 

window = Tk()
window.title("my first GUI program")
window.minsize(500,500)

#label

my_label = Label(text="i am a label",font=("Arial",24,"bold"))
my_label.pack()

my_label["text"]="new text"
my_label.config(text="new text")

#button

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

    
button = Button(text="clicked Me",command=button_clicked)
button.pack()

#entry

input = Entry(width=10)
input.pack()
print(input.get())
 






window.mainloop()