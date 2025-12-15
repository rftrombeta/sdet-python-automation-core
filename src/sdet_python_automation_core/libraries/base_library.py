from robot.api.deco import keyword
from sdet_python_automation_core.services.http.http_client import HttpClient
from sdet_python_automation_core.core.config.loader import ConfigLoader
import uuid


class BaseLibrary:

    def __init__(self):
        self.client = None
        self.last_response = None
        self.user_email = None
        self.user_password = "123456"

    @keyword("Create HTTP Client From Config")
    def create_http_client_from_config(self):
        config = ConfigLoader().load()
        self.client = HttpClient(
            base_url=config["http"]["base_url"],
            timeout=config["http"].get("timeout", 30),
            verify_ssl=config["http"].get("verify_ssl", True)
        )

    @keyword("Criar Usuário ServeRest")
    def criar_usuario_serverest(self):
        self.user_email = f"user_{uuid.uuid4()}@qa.com"

        payload = {
            "nome": "Usuario QA",
            "email": self.user_email,
            "password": self.user_password,
            "administrador": "true"
        }

        self.last_response = self.client.post("/usuarios", json=payload)

    @keyword("Login ServeRest")
    def login_serverest(self):
        payload = {
            "email": self.user_email,
            "password": self.user_password
        }

        self.last_response = self.client.post("/login", json=payload)

    @keyword("Validar Status Code")
    def validar_status_code(self, expected_status):
        assert self.last_response.status_code == int(expected_status), (
            f"Esperado {expected_status}, recebido {self.last_response.status_code}"
        )
