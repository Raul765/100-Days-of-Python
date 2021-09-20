import datetime as dt
import random
import smtplib
import my_secrets

MY_EMAIL = my_secrets.EMAIL
MY_PASSWORD = my_secrets.PASSWORD
SMTP_CONNECTION = "smtp.gmail.com"
recipient_email = MY_EMAIL

now = dt.datetime.now()

#send random quote
def random_quote():
    if now.weekday() == 6:
        with open(r"Day32 - Birthday Wisher\quotes.txt","r") as quote_list:
            quotes = quote_list.readlines()
            quote = random.choice(quotes)

        with smtplib.SMTP(SMTP_CONNECTION) as smtp_conection:
            smtp_conection.starttls()

            smtp_conection.login(MY_EMAIL,MY_PASSWORD)
            smtp_conection.sendmail(from_addr=MY_EMAIL,
                to_addrs=recipient_email, 
                msg=f"Subject:Sunday inspirational quote \n\n {quote}")
            
        
        

random_quote()