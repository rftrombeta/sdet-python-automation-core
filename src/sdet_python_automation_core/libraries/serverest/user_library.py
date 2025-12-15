from robot.api.deco import keyword
import uuid


class ServeRestUserLibrary:
    ROBOT_LIBRARY_SCOPE = "SUITE"

    def __init__(self, base_library):
        self.base = base_library
        self.user_id = None
        self.user_email = None
        self.user_password = "123456"

    @keyword("Create ServeRest User")
    def create_user(self):
        self.user_email = f"user_{uuid.uuid4()}@qa.com"

        payload = {
            "nome": "Usuario QA",
            "email": self.user_email,
            "password": self.user_password,
            "administrador": "true"
        }

        self.base.last_response = self.base.client.post(
            "/usuarios", json=payload
        )

        if self.base.last_response.status_code == 201:
            self.user_id = self.base.last_response.json().get("_id")

    @keyword("Get ServeRest User By Id")
    def get_user_by_id(self):
        self.base.last_response = self.base.client.get(
            f"/usuarios/{self.user_id}"
        )

    @keyword("Update ServeRest User")
    def update_user(self):
        payload = {
            "nome": "Usuario QA Atualizado",
            "email": self.user_email,
            "password": self.user_password,
            "administrador": "true"
        }

        self.base.last_response = self.base.client.put(
            f"/usuarios/{self.user_id}", json=payload
        )

    @keyword("Delete ServeRest User")
    def delete_user(self):
        self.base.last_response = self.base.client.delete(
            f"/usuarios/{self.user_id}"
        )
