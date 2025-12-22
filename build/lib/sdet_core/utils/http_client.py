# src/sdet_core/utils/http_client.py
import requests

class RestClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def set_auth_token(self, token):
        """Método útil para injetar o token JWT na sessão atual"""
        self.session.headers.update({"Authorization": f"{token}"})

    def post(self, endpoint, payload=None):
        return self.session.post(f"{self.base_url}{endpoint}", json=payload)

    def get(self, endpoint, params=None):
        return self.session.get(f"{self.base_url}{endpoint}", params=params)