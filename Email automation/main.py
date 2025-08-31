import smtplib
import datetime as dt 
import random
from dotenv import load_dotenv
import os

load_dotenv()
my_email = os.getenv("MY_EMAIL")
my_password = os.getenv("MY_PASSWORD")

now = dt.datetime.now()
year = now.year
day = now.day
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)    

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() #for encrytption at transport layer
        connection.login(user=my_email,password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="jharivichu27@gmail.com",
            msg = f"Subject:Monday Motivation\n\n{quote}"
        )
