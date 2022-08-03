from twilio.rest import Client

account_sid = "acc_sid"
auth_token = "token"
FROM_NO = "+from"
TO_NO = "+to"


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
