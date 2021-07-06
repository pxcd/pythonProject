import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 14.599512 # Your latitude
MY_LONG = 120.984222 # Your longitude
MARGIN = 5
TZ_OFFSET = 8
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
my_email = ""
password = ""
iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


time_now = datetime.now()



#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


def is_iss_near():
    if iss_latitude >= MY_LAT + MARGIN or iss_latitude >= MY_LAT - MARGIN:
        if iss_longitude >= MY_LAT + MARGIN or iss_longitude >= MY_LAT - MARGIN:
            return True
    else:
        return False


def is_it_nighttime():
    if sunset + TZ_OFFSET >= time_now.hour and sunrise + TZ_OFFSET <= time_now.hour:
        return True
    else:
        return False


def alert_me():
    with smtplib.SMTP("smtp.gmail.com", "587") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:ISS is near!\n\nLOOK UP!!"
        )


while True:
    if is_iss_near() and is_it_nighttime():
        alert_me()
    time.sleep(60)

