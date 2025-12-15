from robot.api.deco import keyword
from sdet_python_automation_core.services.http.http_client import HttpClient
from sdet_python_automation_core.core.config.loader import ConfigLoader


class BaseLibrary:
    ROBOT_LIBRARY_SCOPE = "SUITE"

    def __init__(self):
        self.client = None
        self.last_response = None

    @keyword("Create HTTP Client From Config")
    def create_http_client_from_config(self):
        config = ConfigLoader().load()
        self.client = HttpClient(
            base_url=config["http"]["base_url"],
            timeout=config["http"].get("timeout", 30),
            verify_ssl=config["http"].get("verify_ssl", True)
        )

    @keyword("Status Code Should Be")
    def status_code_should_be(self, expected_status):
        assert self.last_response.status_code == int(expected_status), (
            f"Esperado {expected_status}, recebido {self.last_response.status_code}"
        )
