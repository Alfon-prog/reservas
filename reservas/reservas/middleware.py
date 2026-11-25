import logging

logger= logging.getLogger("reservas.peticiones")

class RegistroPeticionesMiddleware:

    def __init__(self, get_response):

        """
        Configuración inicial del middleware. 
        Se ejecuta una sola vez cuando se arranca el servidor.
        """

        self.get_response = get_response

    def __call__(self, request):

            """
            Código que se ejecuta por cada petición antes y después 
            de que se procese en la vista.
            """

            response= self.get_response(request)

            if request.user.is_authenticated:
                usuario= request.user.username
            else:
                usuario= "anonimo"

            logger.info(f"{request.method} {request.path} {response.status_code} {usuario}")

            return response