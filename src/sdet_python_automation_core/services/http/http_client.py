# src/sdet_python_automation_core/services/http/http_client.py

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from sdet_python_automation_core.services.http.http_response import HttpResponse


class HttpClient:
    def __init__(
        self,
        base_url: str = "",
        headers: dict | None = None,
        timeout: int = 10,
        retries: int = 3,
        backoff_factor: float = 0.3
    ):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

        self.session = requests.Session()

        if headers:
            self.session.headers.update(headers)

        retry_strategy = Retry(
            total=retries,
            backoff_factor=backoff_factor,
            status_forcelist=[500, 502, 503, 504],
            allowed_methods=["GET", "POST", "PUT", "DELETE", "PATCH"]
        )

        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

    def _build_url(self, endpoint: str) -> str:
        if endpoint.startswith("http"):
            return endpoint
        return f"{self.base_url}/{endpoint.lstrip('/')}"

    def get(self, endpoint: str, params: dict | None = None) -> HttpResponse:
        response = self.session.get(
            self._build_url(endpoint),
            params=params,
            timeout=self.timeout
        )
        return HttpResponse(response)

    def post(self, endpoint: str, json: dict | None = None, data=None) -> HttpResponse:
        response = self.session.post(
            self._build_url(endpoint),
            json=json,
            data=data,
            timeout=self.timeout
        )
        return HttpResponse(response)

    def put(self, endpoint: str, json: dict | None = None) -> HttpResponse:
        response = self.session.put(
            self._build_url(endpoint),
            json=json,
            timeout=self.timeout
        )
        return HttpResponse(response)

    def delete(self, endpoint: str) -> HttpResponse:
        response = self.session.delete(
            self._build_url(endpoint),
            timeout=self.timeout
        )
        return HttpResponse(response)
