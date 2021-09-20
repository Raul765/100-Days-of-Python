from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#label

my_label = Label(text="I am a label", font=("Arian",24,"bold"))
my_label.grid(column=0,row=0)

#button

def button_clicked():
    my_label["text"]=input.get()

button = Button(text="Click Me",command=button_clicked)
button.grid(column=1,row=1)

new_button = Button(text="Click Me",command=button_clicked)
new_button.grid(column=2,row=0)

#entry

input = Entry(width=10)
input.grid(column=3,row=2)








window.mainloop()