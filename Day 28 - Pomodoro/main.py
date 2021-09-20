from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
stop=False
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global stop
    global reps 

    start.config(command=start_timer)
    stop = True
    reps=0
    check_marks.config(text="")
    canvas.itemconfig(timer_text,text="00:00")
    title.config(text="Timer")

    



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps 
    global stop

    stop = False

    start.config(command=nothing)
    reps +=1
    if reps%2 != 0:
        countdown(WORK_MIN*60)
        title.config(text="Work", fg=GREEN)
    elif reps%8 ==0:
        countdown(LONG_BREAK_MIN*60)
        title.config(text="Rest", fg=RED)
    else:
        countdown(SHORT_BREAK_MIN*60)
        title.config(text="Rest", fg=PINK)

    if reps%2==0:
        add_check_mark()

def nothing():
    pass

def add_check_mark():
    global reps
    check_marks.config(text="✓"*math.floor(reps/2))
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global stop

    if stop==False:
        minutes=math.floor(count/60)
        if minutes < 10:
            minutes=f"0{minutes}"
        seconds=count%60
        if seconds < 10:
            seconds=f"0{seconds}"
        canvas.itemconfig(timer_text,text=f"{minutes}:{seconds}")
    
        if count > 0:
            window.after(1000, countdown, count-1 )
        else:
            start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50,bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=r"Dy28 - a\tomato.png")
canvas.create_image(100,112, image=tomato_img)
canvas.grid(row=1,column=1)

timer_text = canvas.create_text(102,130, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))

title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME,35,"bold"))
title.grid(row=0, column=1)

check_marks = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME,13,"bold"))
check_marks.grid(row=3, column=1)

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(row=2, column=2)

window.mainloop()