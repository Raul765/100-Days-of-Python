##################### Extra Hard Starting Project ######################
# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.

import random
import pandas 
import datetime as dt
import smtplib
import my_secrets

BIRTHDAY_LIST_PATH = r"Day32 - Birthday Wisher\birthday-wisher-extrahard-start\birthdays.csv"

LETTER1_PATH = r"Day32 - Birthday Wisher\birthday-wisher-extrahard-start\letter_templates\letter_1.txt"
LETTER2_PATH = r"Day32 - Birthday Wisher\birthday-wisher-extrahard-start\letter_templates\letter_2.txt"
LETTER3_PATH = r"Day32 - Birthday Wisher\birthday-wisher-extrahard-start\letter_templates\letter_3.txt"

MY_EMAIL = my_secrets.EMAIL
MY_PASSWORD = my_secrets.PASSWORD
SMTP_CONNECTION = "smtp.gmail.com"

now = dt.datetime.now()
letter_list = [LETTER1_PATH, LETTER2_PATH, LETTER3_PATH]

with open(BIRTHDAY_LIST_PATH,"r") as birthday_data:
    birthday_list = pandas.read_csv(birthday_data)

    people_to_write_to = []
    for person in birthday_list["name"]:
        if int(birthday_list[birthday_list["name"]==person]["day"])==now.day and int(birthday_list[birthday_list["name"]==person]["month"])==now.month:
            people_to_write_to.append(person)

    if len(people_to_write_to)>0:
        with smtplib.SMTP(SMTP_CONNECTION) as conection:
            conection.starttls()
            conection.login(MY_EMAIL,MY_PASSWORD)

            for person in people_to_write_to:
                with open(random.choice(letter_list), "r") as letter_template:
                    letter = letter_template.read()
                    birthday_message = letter.replace("[NAME]", person)
                    conection.sendmail(from_addr=MY_EMAIL,
                        to_addrs=str(birthday_list[birthday_list["name"]==person]["email"]).split()[1], 
                        msg=f"Subject:Happy Birthday! \n\n {birthday_message}")





