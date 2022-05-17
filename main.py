##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import random
import pandas as pd

MY_EMAIL = "hocpythonwithme@gmail.com"
MY_PASSWORD = "Chethanh2803"

# 1. Update the birthdays.csv
data = pd.read_csv("birthdays.csv")
birthday_data = data.to_dict(orient="records")
now = dt.datetime.now()
month = now.month
day = now.day
# 2. Check if today matches a birthday in the birthdays.csv
for person in birthday_data:
    if person["day"] == day and person["month"] == month:
        file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
        with open(file_path) as letter:
            content = letter.read()
            content = content.replace("[NAME]", person["name"])
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=person["email"],
                                msg=f"Subject:Happy Birthday\n\n{content}"
                                )





