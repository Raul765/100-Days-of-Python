import requests
import smtplib
import time
import my_secrets

from datetime import datetime
from datetime import timezone

MY_LAT = my_secrets.COORDINATES["lat"]
MY_LONG = my_secrets.COORDINATES["long"]

MY_EMAIL = my_secrets.EMAIL
MY_PASSWORD = my_secrets.PASSWORD
SMTP_CONNECTION = "smtp.gmail.com"

now = datetime.now(tz=timezone.utc)

def ISS_near():
    response1 = requests.get(url=r"http://api.open-notify.org/iss-now.json")
    response1.raise_for_status()
    
    data = response1.json()["iss_position"]
    if MY_LAT-5 <= float(data["latitude"]) <= MY_LAT+5  and  MY_LONG-5 <= float(data["longitude"]) <= MY_LONG+5:
            return True
    

def check_if_dark():
    parameters = {
        "lat":MY_LAT,
        "lng":MY_LONG,
        "formatted":0,
    }

    response2 = requests.get(url=r"https://api.sunrise-sunset.org/json", params=parameters)
    response2.raise_for_status()

    data = response2.json()
    sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    now_hour = now.hour

    if now_hour >= sunset_hour and now_hour < sunrise_hour:
        return True

while True:
    if ISS_near() and check_if_dark():
        with smtplib.SMTP(SMTP_CONNECTION) as connection:
            connection.starttls()
            connection.login(MY_EMAIL,MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addr=MY_EMAIL, msg="Subject:Look Up! \n\n The ISS is above you in the sky")
    time.sleep(60)