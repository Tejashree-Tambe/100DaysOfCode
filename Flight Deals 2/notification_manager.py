from twilio.rest import Client
import smtplib

TWILIO_SID = "sid"
TWILIO_AUTH_TOKEN = "token"
TWILIO_VIRTUAL_NUMBER = "+to"
TWILIO_VERIFIED_NUMBER = "+from"

MY_EMAIL = "email@gmail.com"
PASSWORD = "password"


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
