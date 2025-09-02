import requests
import datetime as dt
import smtplib
import os 
from dotenv import load_dotenv
import time
load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
MY_LAT = 8.539340
MY_LONG = 76.983269

parameters = {
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0
}

def is_iss_overhead():
    issresponse = requests.get("http://api.open-notify.org/iss-now.json")
    issresponse.raise_for_status()
    issdata = issresponse.json()
    isslat = float(issdata["iss_position"]["latitude"])
    isslng = float(issdata["iss_position"]["longitude"])
    if MY_LAT-5<=isslat<=MY_LAT+5 and MY_LONG-5<=isslng<=MY_LONG+5:
        return True

def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) #we only need hour so that we can compare and ensure sky is dark 
    sunset =  int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = dt.datetime.now()
    hour_now = int(time_now.hour)
    if hour_now>=sunset and hour_now<=sunrise:
        return True 
while True:
    time.sleep(60)
    if is_night() and is_iss_overhead():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg = "subject: LOOK UP\n\nThe ISS is above your sky.",
        )
        
