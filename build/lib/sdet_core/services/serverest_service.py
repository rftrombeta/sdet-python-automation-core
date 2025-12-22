# src/sdet_core/services/serverest_service.py
from sdet_core.utils import ConfigLoader
from sdet_core.utils import RestClient

class ServeRestService:
    def __init__(self, config_file="config.yaml"):
        self.config = ConfigLoader(config_file)
        # O Service agora é dinâmico!
        self.client = RestClient(self.config.get_base_url())

    def realizar_login(self, email, password):
        payload = {"email": email, "password": password}
        return self.client.post("/login", payload)

    def cadastrar_usuario(self, nome, email, password, administrador="true"):
        payload = {
            "nome": nome, "email": email, 
            "password": password, "administrador": administrador
        }
        return self.client.post("/usuarios", payload)