import requests
import smtplib
import my_secrets
#-------------------- Weather API setup

API_KEY = my_secrets.OPENWEATHERMAP_KEY
CITY = my_secrets.CITY
STATE_CODE = my_secrets.STATE_CODE
COUNTRY_CODE = my_secrets.COUNTRY_CODE

parameters ={
    "lat": my_secrets.COORDINATES["lat"],
    "lon": my_secrets.COORDINATES["long"],
    "appid": API_KEY,
    "exclude": "current,minutely,daily,alerts",
    "lang": "sp",
}

response = requests.get(url=r"https://api.openweathermap.org/data/2.5/onecall",params=parameters)
response.raise_for_status()

data = response.json()

#-------------------- SMTP Setup

MY_EMAIL = my_secrets.EMAIL
MY_PASSWORD = my_secrets.PASSWORD
SMTP_CONNECTION = "smtp.gmail.com"

#-------------------- Functions

end=False

for i in range(12):
    if not end:
        for j in data["hourly"][i]["weather"]:
            if int(j["id"])<700:
                with smtplib.SMTP(SMTP_CONNECTION) as connection:
                    connection.starttls()
                    connection.login(MY_EMAIL,MY_PASSWORD)
                    connection.sendmail(from_addr=MY_EMAIL, to_addr=MY_EMAIL, msg="Subject:Don't forget your umbrella! \n\n Rain is expected in the following 12 hours")
                end=True
                break
    else:
        break


