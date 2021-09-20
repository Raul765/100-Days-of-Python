from tkinter import *

window = Tk()
window.title("Widget Examples")
window.config(padx=10, pady=10)

entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(row=0,column=1)

miles=Label(text="Miles")
miles.grid(row=0,column=2)

equal = Label(text="is equal to")
equal.grid(row=1,column=0)

result = Label(text="0")
result.grid(row=1,column=1)

km = Label(text="km")
km.grid(row=1,column=2)

def calculate():
    result["text"]= float(entry.get())*1.609344 

button = Button(text="Calculate", command=calculate)
button.grid(row=2,column=1)

window.mainloop()