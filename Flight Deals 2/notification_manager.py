from twilio.rest import Client
import smtplib

TWILIO_SID = "AC1abdc7ac82c6feba7a86c37f42d6f192"
TWILIO_AUTH_TOKEN = "71a1122b85cc63c0bc54f63050323cd2"
TWILIO_VIRTUAL_NUMBER = "+15207292541"
TWILIO_VERIFIED_NUMBER = "+919930049115"

MY_EMAIL = "pythondeveloper0401@gmail.com"
PASSWORD = "Python123"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            email_message = f"Subject: New low price alert!\n\n{message}\n{google_flight_link}".encode('utf-8')
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=email_message
                )
