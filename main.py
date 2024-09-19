from app_request import AppRequest

from twilio_config import TwilioConfig

app_request = AppRequest()
twilio_client = TwilioConfig()


def get_crypto_price():
    path = "simple/price"
    params = {
        'ids': 'bitcoin,ethereum,binancecoin',
        'vs_currencies': 'usd'
    }
    return app_request.get(path, params)


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
    message = f"ALERTA: {name} ha superado los ${threshold} USD, su precio actual es ${price} USD."
    twilio_client.send_message(message)


def main():
    try:
        prices = get_crypto_price()
        check_price_and_alert(prices)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
