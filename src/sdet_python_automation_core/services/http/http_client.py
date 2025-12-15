import requests

class HttpClient:

    def __init__(self, base_url, timeout=30, verify_ssl=True):
        self.base_url = base_url
        self.timeout = timeout
        self.verify_ssl = verify_ssl
        self.headers = {}

    def post(self, endpoint, json=None):
        return requests.post(
            url=f"{self.base_url}{endpoint}",
            json=json,
            headers=self.headers,
            timeout=self.timeout,
            verify=self.verify_ssl
        )
