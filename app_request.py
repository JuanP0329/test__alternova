import requests
from dotenv import dotenv_values

from request_error import RequestError

properties = dotenv_values(".env")


class AppRequest:

    def get(self, path, params):
        try:
            response = requests.get(f"{properties["HOST"]}{path}", params=params)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise RequestError(f"Error al realizar la petición: {e}")
