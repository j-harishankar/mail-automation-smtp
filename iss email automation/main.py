import requests
import datetime as dt
import smtplib
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
    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0] #we only need hour so that we can compare and ensure sky is dark 
    sunset =  data["results"]["sunset"].split("T")[1].split(":")[0]
    time_now = dt.datetime.now()
    hour_now = time_now.hour
    if time_now<=sunset and time_now>=sunrise:
        return True 


    
