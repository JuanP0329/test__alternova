class RequestError(Exception):
    """
    Excepción personalizada para manejar errores relacionados con las peticiones a la API.

    Args:
        message (str): Mensaje descriptivo del error.
    """
    def __init__(self, message):
        """
        Inicializa la excepción con un mensaje de error.

        Args:
            message (str): Mensaje que describe el error ocurrido.
        """
        self.message = message