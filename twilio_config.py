from dotenv import dotenv_values
from twilio.rest import Client

# Carga las variables de entorno desde el archivo .env
properties = dotenv_values(".env")


class TwilioConfig:
    """
    Clase que gestiona la configuración y el envío de mensajes mediante la API de Twilio.
    Obtiene las credenciales y los números de teléfono desde el archivo .env.
    """

    def __init__(self):
        """
        Inicializa la configuración de Twilio con las credenciales y números de teléfono
        necesarios para enviar mensajes por WhatsApp.

        Las siguientes variables se obtienen del archivo .env:
        - TWILIO_ACCOUNT_SID: ID de cuenta de Twilio.
        - TWILIO_AUTH_TOKEN: Token de autenticación de Twilio.
        - TWILIO_WHATSAPP_NUMBER: Número de WhatsApp configurado en Twilio.
        - YOUR_PHONE_NUMBER: Tu número de WhatsApp verificado para recibir los mensajes.
        """
        self.twilio_account_sid = properties["TWILIO_ACCOUNT_SID"]
        self.twilio_auth_token = properties["TWILIO_AUTH_TOKEN"]
        self.twilio_whatsapp_number = f'whatsapp:{properties["TWILIO_WHATSAPP_NUMBER"]}'
        self.your_whatsapp_number = f'whatsapp:{properties["YOUR_PHONE_NUMBER"]}'

    def send_message(self, message):
        """
        Envía un mensaje de WhatsApp utilizando la API de Twilio.

        Args:
            message (str): El contenido del mensaje que será enviado por WhatsApp.
        """
        client = Client(self.twilio_account_sid, self.twilio_auth_token)
        client.messages.create(
            from_=self.twilio_whatsapp_number,
            body=message,
            to=self.your_whatsapp_number
        )
