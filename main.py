import requests
from dotenv import dotenv_values
from twilio.rest import Client

properties = dotenv_values(".env")

twilio_account_sid = properties["TWILIO_ACCOUNT_SID"]
twilio_auth_token = properties["TWILIO_AUTH_TOKEN"]
twilio_whatsapp_number = 'whatsapp:+14155238886'
your_whatsapp_number = 'whatsapp:+573152020197'


def get_crypto_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': 'bitcoin,ethereum,binancecoin',
        'vs_currencies': 'usd'
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def check_price_and_alert(prices):
    thresholds = {
        'bitcoin': (30000, 'Bitcoin'),
        'ethereum': (2000, 'Ethereum'),
        'binancecoin': (300, 'Binace Coin')
    }

    for crypto, (threshold, name) in thresholds.items():
        current_price = prices[crypto]['usd']
        if current_price > threshold:
            send_whatsapp_alert(name, threshold, current_price)


def send_whatsapp_alert(name, threshold, price):
    client = Client(twilio_account_sid, twilio_auth_token)
    message = f"ALERTA: {name} ha superado los ${threshold} USD, su precio actual es ${price} USD."

    client.messages.create(
        from_=twilio_whatsapp_number,
        body=message,
        to=your_whatsapp_number
    )


def main():
    try:
        prices = get_crypto_price()
        check_price_and_alert(prices)
    except Exception:
        print("ERROR: Problema al obtener los precios de las criptomonedas.")


if __name__ == "__main__":
    main()
