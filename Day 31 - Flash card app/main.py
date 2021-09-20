from tkinter import *
import pandas
import random

#Constants
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_TO_LEARN = "French"
LANGUAGE_USED = "English"

WORD_LIST_PATH = r"Day31 - Flash card app\data\french_words.csv"
WORDS_TO_LEARN_PATH = r"Day31 - Flash card app\data\words to learn.csv"

CARD_FRONT_PATH = r"Day31 - Flash card app\images\card_front.png"
CARD_BACK_PATH = r"Day31 - Flash card app\images\card_back.png"
RIGTH_SYMBOL_PATH = r"Day31 - Flash card app\images\right.png"
WRONG_SYMBOL_PATH = r"Day31 - Flash card app\images\wrong.png"

TIME = 2000

#Word List
try:
    word_list = pandas.read_csv(WORDS_TO_LEARN_PATH)

except:
    word_list = pandas.read_csv(WORD_LIST_PATH)

finally:
    words_to_learn=[]
    for word in word_list[LANGUAGE_TO_LEARN]:
        words_to_learn.append(word)

    meanings_to_learn=[]
    for word in word_list[LANGUAGE_USED]:
        meanings_to_learn.append(word)

    new_word_list={
        LANGUAGE_TO_LEARN: words_to_learn,
        LANGUAGE_USED: meanings_to_learn,
    }

    data = pandas.DataFrame(new_word_list)
    data.to_csv(WORDS_TO_LEARN_PATH)

#Functions
def new_word():
    global word_number, timer

    window.after_cancel(timer)

    word_number = random.randint(0,len(new_word_list[LANGUAGE_TO_LEARN])-1)

    canvas.itemconfig(card, image=card_front)
    canvas.itemconfig(title, text=LANGUAGE_TO_LEARN)
    canvas.itemconfig(word, text=new_word_list[LANGUAGE_TO_LEARN][word_number])

    timer = window.after(TIME, see_answer)  
    
def see_answer():
    canvas.itemconfig(card,image=card_back)
    canvas.itemconfig(title,text=LANGUAGE_USED)
    canvas.itemconfig(word,text=new_word_list[LANGUAGE_USED][word_number])

def knew_the_answer():
    global new_word_list

    new_word_list[LANGUAGE_TO_LEARN].pop(word_number)
    new_word_list[LANGUAGE_USED].pop(word_number)
    
    data = pandas.DataFrame(new_word_list)
    data.to_csv(WORDS_TO_LEARN_PATH)

    new_word()

#Settings
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=525, width=820, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front = PhotoImage(file=CARD_FRONT_PATH)
card_back = PhotoImage(file=CARD_BACK_PATH)
right = PhotoImage(file=RIGTH_SYMBOL_PATH)
wrong = PhotoImage(file=WRONG_SYMBOL_PATH)

#UI
word_number = random.randint(0,len(new_word_list[LANGUAGE_TO_LEARN])-1)
timer = window.after(TIME, see_answer)

card = canvas.create_image(415,263, image=card_front)
title = canvas.create_text(400,150, text=LANGUAGE_TO_LEARN, font=("Arial", 40, "italic"))
word = canvas.create_text(400,263, text=new_word_list[LANGUAGE_TO_LEARN][word_number], font=("Arial", 60, "bold"))
canvas.grid(row=0,column=0,columnspan=2)

right_button = Button(image=right, highlightthickness=0, command=knew_the_answer)
right_button.grid(row=1,column=1)

wrong_button = Button(image=wrong, highlightthickness=0, command=new_word)
wrong_button.grid(row=1,column=0)

window.mainloop()