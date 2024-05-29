from twilio.rest import Client

TWILIO_SID = "AC0040c2106180fa8bbfb4de23fce48211"
TWILIO_AUTH_TOKEN = "aa3b6bf830f6aff3a0729e73bd52bca8"
TWILIO_VIRTUAL_NUMBER = "+18624658085"
TWILIO_VERIFIED_NUMBER = "+971 56 901 6550"


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
        #print(message.sid)