import requests
from dotenv import dotenv_values

# Carga las propiedades y variables de entorno desde el archivo .env
from request_error import RequestError

properties = dotenv_values(".env")


class AppRequest:
    """
    Clase que encapsula la lógica para realizar peticiones HTTP a la API.
    Utiliza las propiedades definidas en el archivo .env para configurar el host.
    """
    def get(self, path, params):
        """
        Realiza una petición GET a la API definida por la propiedad HOST en el archivo .env.
        
        Args:
            path (str): Ruta del endpoint de la API a la que se quiere acceder.
            params (dict): Parámetros que se enviarán junto a la solicitud GET.
        
        Returns:
            dict: La respuesta de la API en formato JSON, si la petición es exitosa.
        
        Raises:
            RequestError: Si ocurre un error en la petición, se lanza una excepción personalizada.
        """
        try:
            response = requests.get(f"{properties["HOST"]}{path}", params=params)
            response.raise_for_status() # Verifica si la respuesta fue exitosa (código 2xx).
            return response.json()
        except Exception as e:
            # Captura cualquier excepción y lanza un error personalizado
            raise RequestError(f"Error al realizar la petición: {e}")
