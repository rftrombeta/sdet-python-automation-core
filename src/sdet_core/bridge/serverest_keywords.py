# src/sdet_core/services/serverest_service.py
from sdet_core.utils import RestClient

class ServeRestService:
    def __init__(self):
        # Base URL do ServeRest fixa ou vinda de um arquivo de config YAML
        self.client = RestClient("https://serverest.dev")

    def autenticar_e_salvar_sessao(self, email, password):
        payload = {"email": email, "password": password}
        response = self.client.post("/login", payload)
        
        if response.status_code == 200:
            token = response.json().get("authorization")
            self.client.set_auth_token(token)
            return True
        return False

    def listar_usuarios(self):
        # Esta chamada já enviará o Token automaticamente se o login foi feito
        return self.client.get("/usuarios")