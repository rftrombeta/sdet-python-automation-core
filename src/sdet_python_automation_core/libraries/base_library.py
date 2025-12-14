# src/sdet_python_automation_core/libraries/base_library.py

from robot.api.deco import keyword

from sdet_python_automation_core.core.context.execution_context import ExecutionContext
from sdet_python_automation_core.services.http.http_client import HttpClient


class BaseLibrary:
    """Base Robot Framework Library for API automation"""

    def __init__(self):
        self.context = ExecutionContext()

    @keyword("Create HTTP Client")
    def create_http_client(self, base_url: str, timeout: int = 10):
        """
        Creates and stores a HTTP client instance
        """
        self.context.http_client = HttpClient(
            base_url=base_url,
            timeout=timeout
        )

    @keyword("GET")
    def get(self, endpoint: str):
        self._ensure_client()
        response = self.context.http_client.get(endpoint)
        self.context.last_response = response
        return response.text

    @keyword("POST")
    def post(self, endpoint: str, payload: dict):
        self._ensure_client()
        response = self.context.http_client.post(endpoint, json=payload)
        self.context.last_response = response
        return response.text

    @keyword("Status Should Be")
    def status_should_be(self, expected_status: int):
        if not self.context.last_response:
            raise AssertionError("No HTTP response available")

        actual = self.context.last_response.status_code
        if actual != expected_status:
            raise AssertionError(
                f"Expected status {expected_status}, got {actual}"
            )

    def _ensure_client(self):
        if not self.context.http_client:
            raise RuntimeError("HTTP Client not created. Use 'Create HTTP Client' first.")
