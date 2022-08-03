import smtplib

my_email = "pythondeveloper0401@gmail.com"
password = "Python123"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs="manesheetal102@gmail.com",
    msg="Subject: Hello\n\nHi! Hello")
connection.close()
