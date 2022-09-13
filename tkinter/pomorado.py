from cgitb import text
from itertools import count
from tabnanny import check
from tkinter import *
import math
#-------------------constants------------
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_TIME = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

#------------------timer reset-----------------

def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title_label.config(text="Timer" , fg=GREEN)
    check_marks.config(text="",fg=GREEN,bg=YELLOW)

    
#-------------------timer mechanism--------------------

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_TIME * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0 :
        count_down(long_break_sec)
        title_label.config(text="break" ,fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="break",fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="work" , fg= GREEN)

#------------------countdown mechanism-------------------

def count_down(count):
    count_min = math.floor(count / 60 )
    count_sec = count % 60

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0 :
        global timer
        timer = window.after(1000 , count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔"
        check_marks.config(text = marks)

#------------------UI SETUP-------------------
window = Tk()
window.title("Pomorado")
window.config(padx=100 , pady=20 , bg=YELLOW)

canvas = Canvas(width=250, height=250 , bg=YELLOW , highlightthickness=0)
tomato_img = PhotoImage(file = "tkinter\orange.png")
canvas.create_image(120, 120 , image=tomato_img)

title_label = Label(text="Timer",font=("Arial",50,"bold"),fg=GREEN,bg=YELLOW)
title_label.grid(column = 1, row = 0)

timer_text = canvas.create_text(120, 150 , text="00:00" , fill="white" , font=(FONT_NAME,30,"bold"))
canvas.grid(column = 1, row = 1)

start_button = Button(text="    start    ",command=start_timer , highlightthickness=0)
start_button.grid(column=0,row=2)

reset_button = Button(text="    reset    ",command=reset_timer, highlightthickness=0)
reset_button.grid(column=2,row=2)

check_marks = Label(text="✔",fg=GREEN,bg=YELLOW)
check_marks.grid(column=1,row=3)








window.mainloop()