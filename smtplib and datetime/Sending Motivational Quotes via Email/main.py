import datetime as dt
import smtplib
import random

try:
    with open("quotes.txt") as data_file:
        data = data_file.readlines()

except FileNotFoundError:
    print("File doesn't exist")

todays_quote = random.choice(data)

now = dt.datetime.now()
day_of_week = now.weekday()

my_email = "mail"
password = "password"
subject = "Today's motivational quote"
message = f"Hey there!\n\n Today's motivational quote is:\n {todays_quote}"

if day_of_week == 2:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="to",
            msg=f"Subject:{subject}\n\n{message}")
