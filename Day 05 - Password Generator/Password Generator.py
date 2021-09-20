import random

letters="abcdefghijklmnopqrstuvwxyz"
numbers="1234567890"
symbols="<>'?¿!¡\*+}]{[()&%$#"

print("Welcome to the password generator!")

n_letters_upper =int(input("How many upper case letters would you like in your password?\n"))
n_letters_lower=int(input("How many lower case letters would you like in your password?\n"))
n_numbers=int(input("How many numbers would you like in your password?\n"))
n_symbols=int(input("How many symbols would you like in your password?\n"))

password=[]

for i in range(n_letters_upper):
    password.append(random.choice(letters).upper())
for i in range(n_letters_lower):
    password.append(random.choice(letters))
for i in range(n_numbers):
    password.append(random.choice(numbers))
for i in range(n_symbols):
    password.append(random.choice(symbols))

random.shuffle(password)
password ="".join(password)

print (f"Your password is: {password}")