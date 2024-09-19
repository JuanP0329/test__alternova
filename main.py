from app_request import AppRequest

from twilio_config import TwilioConfig

# Inicializa las instancias para realizar peticiones y configurar Twilio
app_request = AppRequest()
twilio_client = TwilioConfig()


def get_crypto_price():
    """
    Obtiene los precios actuales en USD de Bitcoin, Ethereum y Binance Coin
    utilizando la API de CoinGecko.

    Returns:
        dict: Un diccionario con los precios actuales de las criptomonedas.
    """
    path = "simple/price"
    params = {
        'ids': 'bitcoin,ethereum,binancecoin',
        'vs_currencies': 'usd'
    }
    return app_request.get(path, params)


def check_price_and_alert(prices):
    """
    Verifica si los precios de las criptomonedas han superado ciertos umbrales
    y envía una alerta a través de WhatsApp si es necesario.

    Args:
        prices (dict): Diccionario con los precios de las criptomonedas.
    """
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
    """
    Envía una alerta vía WhatsApp cuando el precio de una criptomoneda
    supera el umbral definido.

    Args:
        name (str): Nombre de la criptomoneda.
        threshold (int): Umbral de precio definido.
        price (float): Precio actual de la criptomoneda.
    """
    message = f"ALERTA: {name} ha superado los ${threshold} USD, su precio actual es ${price} USD."
    twilio_client.send_message(message)


def main():
    """
    Función principal que orquesta el flujo del programa:
    - Obtiene los precios de las criptomonedas.
    - Verifica si han superado los umbrales.
    - Envía una alerta si es necesario.
    """
    try:
        prices = get_crypto_price()
        check_price_and_alert(prices)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
