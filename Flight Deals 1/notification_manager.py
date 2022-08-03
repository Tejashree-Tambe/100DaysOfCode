from twilio.rest import Client

account_sid = "AC1abdc7ac82c6feba7a86c37f42d6f192"
auth_token = "71a1122b85cc63c0bc54f63050323cd2"
FROM_NO = "+15207292541"
TO_NO = "+919930049115"


class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=FROM_NO,
            to=TO_NO,
        )

        print(message.sid)
        print("Message sent")
