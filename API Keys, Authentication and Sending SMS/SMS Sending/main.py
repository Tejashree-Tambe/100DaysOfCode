import os
from twilio.rest import Client


account_sid = os.environ['acc_sid']
auth_token = os.environ['auth_token']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+15017122661',
                     to='+15558675310'
                 )

print(message.sid)
