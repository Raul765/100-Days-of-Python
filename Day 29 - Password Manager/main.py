from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generation():
    letters="abcdefghijklmnopqrstuvwxyz"
    numbers="1234567890"
    symbols="<>'?¿!¡\*+}]{[()&%$#"

    n_letters=random.randint(8,10)
    n_letters_lower=random.randint(1,n_letters-1)
    n_letters_upper =n_letters-n_letters_lower
    n_numbers=random.randint(2,4)
    n_symbols=random.randint(2,4)

    new_password=[]

    for i in range(n_letters_upper):
        new_password.append(random.choice(letters).upper())
    for i in range(n_letters_lower):
        new_password.append(random.choice(letters))
    for i in range(n_numbers):
        new_password.append(random.choice(numbers))
    for i in range(n_symbols):
        new_password.append(random.choice(symbols))

    random.shuffle(new_password)
    new_password ="".join(new_password)
    password.delete(0,END)
    password.insert(0,new_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    data_website = website.get()
    data_email = email.get()
    data_password = password.get()

    if len(data_website) == 0 or len(data_email) == 0 or len(data_password) == 0: 
        messagebox.showinfo("Oops", "Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=data_website,message=f"These are the details entered: \n Email: {data_email} \n Password: {data_password} \n Is it OK to save?" )
        if is_ok:
            with open(r"Day29 - Password Manager\data.txt", "a") as text:
                text.write(f"{data_website} | {data_email} | {data_password}\n")
                website.delete(0,END)
                password.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=180)
logo = PhotoImage(file=r"Day29 - Password Manager\logo.png")
canvas.create_image(110,100,image=logo)
canvas.grid(row=0,column=1)

#Labels

label_website = Label(text="Website:")
label_website.grid(row=1, column=0)

label_email = Label(text="Email/Username:")
label_email.grid(row=2, column=0)

label_password = Label(text="Password:")
label_password.grid(row=3, column=0)

#Entries

website = Entry(width=50)
website.grid(row=1, column=1, columnspan=2,sticky="W")
website.focus()

email = Entry(width=50)
email.grid(row=2, column=1, columnspan=2,sticky="W")

password = Entry(width=31)
password.grid(row=3, column=1,sticky="W")

generate_password = Button(text="Generate Password", command=password_generation)
generate_password.grid(row=3, column=2)

add=Button(text="Add", width=42, command=add_data)
add.grid(row=4, column=1, columnspan=2,sticky="W")

window.mainloop()