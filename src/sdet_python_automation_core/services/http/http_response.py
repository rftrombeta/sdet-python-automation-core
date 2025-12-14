# src/sdet_python_automation_core/services/http/http_response.py

class HttpResponse:
    def __init__(self, response):
        self._response = response

    @property
    def status_code(self) -> int:
        return self._response.status_code

    @property
    def headers(self) -> dict:
        return self._response.headers

    @property
    def text(self) -> str:
        return self._response.text

    def json(self):
        return self._response.json()

    def is_success(self) -> bool:
        return 200 <= self.status_code < 300
