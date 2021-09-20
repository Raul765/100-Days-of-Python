from tkinter import *
from tkinter import messagebox
import random
import json

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

# ---------------------------- SAVE DATA ------------------------------- #

def add_data():
    data_website = website.get()
    data_email = email.get()
    data_password = password.get()
    new_data = {
        data_website: {
            "Email": data_email,
            "Password": data_password,
            }
    }
    if len(data_website) == 0 or len(data_email) == 0 or len(data_password) == 0: 
        messagebox.showinfo("Oops", "Please don't leave any fields empty")
    else:
        try:
            with open(r"Day30 - Exception handling and JSON\Password Manager v2\data.json", "r") as data_file:
                data = json.load(data_file)
        except:
            with open(r"Day30 - Exception handling and JSON\Password Manager v2\data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open(r"Day30 - Exception handling and JSON\Password Manager v2\data.json", "w") as data_file:
                data.update(new_data)
                json.dump(data, data_file, indent=4)
        finally:
                website.delete(0,END)
                password.delete(0,END)

# --------------------------- SEARCH DATA ------------------------------- #

def search_data():
    website_data=website.get()
    try:
        with open(r"Day30 - Exception handling and JSON\Password Manager v2\data.json", "r") as data_file: 
            data=json.load(data_file)

            data=data[website_data]  
            password_data=data["Password"]
            email_data=data["Email"]

            messagebox.showinfo(website_data,f"Password: {password_data} \nEmail: {email_data}")

    except:
        messagebox.showinfo("Oops",f"There's no data saved for {website_data}")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=180)
logo = PhotoImage(file=r"Day30 - Exception handling and JSON\Password Manager v2\logo.png")
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

website = Entry(width=30)
website.grid(row=1, column=1, columnspan=2,sticky="W")
website.focus()

email = Entry(width=50)
email.grid(row=2, column=1, columnspan=2,sticky="W")
try:
    with open(r"Day30 - Exception handling and JSON\Password Manager v2\data.json", "r") as data_file: 
        data=json.load(data_file)
        emails=[]
        for key in data:
            emails.append(data[key]["Email"])
        email.insert(0,emails[len(emails) - 1])
except:
    pass


password = Entry(width=30)
password.grid(row=3, column=1,sticky="W")

generate_password = Button(text="Generate Password", command=password_generation, width=15)
generate_password.grid(row=3, column=2, sticky="E")

#Buttons

add = Button(text="Add", width=42, command=add_data)
add.grid(row=4, column=1, columnspan=2,sticky="W")

search = Button(text="Search", command=search_data, width=15)
search.grid(row=1,column=2, sticky="E")

window.mainloop()