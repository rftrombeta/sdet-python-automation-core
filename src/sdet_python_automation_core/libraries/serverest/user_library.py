from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
import uuid


class ServeRestUserLibrary:
    
    def __init__(self):
        self.base = None

    def _get_base(self):
        if not self.base:
            self.base = BuiltIn().get_library_instance(
                "sdet_python_automation_core.libraries.base_library.BaseLibrary"
            )
        return self.base

    @keyword("Create ServeRest User")
    def create_user(self):
        base = self._get_base()

        payload = {
            "nome": "Usuario QA",
            "email": base.user_email,
            "password": base.user_password,
            "administrador": "true"
        }

        base.last_response = base.client.post("/usuarios", json=payload)

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
se