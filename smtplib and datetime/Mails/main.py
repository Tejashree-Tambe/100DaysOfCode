import smtplib

my_email = "mail"
password = "password"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs="to",
    msg="Subject: Hello\n\nHi! Hello")
connection.close()
