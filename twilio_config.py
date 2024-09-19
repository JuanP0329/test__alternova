from dotenv import dotenv_values
from twilio.rest import Client

properties = dotenv_values(".env")

class TwilioConfig:

    def __init__(self):
        self.twilio_account_sid = properties["TWILIO_ACCOUNT_SID"]
        self.twilio_auth_token = properties["TWILIO_AUTH_TOKEN"]
        self.twilio_whatsapp_number = f'whatsapp:{properties["TWILIO_WHATSAPP_NUMBER"]}'
        self.your_whatsapp_number = f'whatsapp:{properties["YOUR_PHONE_NUMBER"]}'

    def send_message(self, message):
        client = Client(self.twilio_account_sid, self.twilio_auth_token)
        client.messages.create(
            from_=self.twilio_whatsapp_number,
            body=message,
            to=self.your_whatsapp_number
        )