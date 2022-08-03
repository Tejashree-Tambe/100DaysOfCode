import datetime as dt
import random
import smtplib
import pandas

MY_EMAIL = "pythondeveloper0401@gmail.com"
PASSWORD = "Python123"
SUBJECT = "Birthday Wish"

# get today's date
todays_date = dt.datetime.now()
today = todays_date.day
this_month = todays_date.month

# check if it matches with anyone's birthday
with open("birthdays.csv") as data_file:
    all_birthdays = pandas.read_csv(data_file)

    for index, row in all_birthdays.iterrows():
        if row.month == this_month and row.day == today:
            name = row["name"]
            sender_email = row.email

# select random letter
letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
letter_template = random.choice(letters)

# send that letter template as mail
with open(f"letter_templates/{letter_template}") as letter_file:
    letter = letter_file.read()
    final_letter = letter.replace("[NAME]", name)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=sender_email,
                            msg=f"Subject:{SUBJECT}\n\n{final_letter}")
