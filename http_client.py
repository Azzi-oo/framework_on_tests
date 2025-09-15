from typing import Any
import requests


class HttpClient:
    
    def __init__(self, url: str):
        # Normalize to always have a single trailing slash
        self.url = url.rstrip('/') + '/'
    
    def request(self, method: str, endpoint: str, **kwargs: Any) -> requests.Response:
        url = f"{self.url}{endpoint}"
        response = requests.request(method, url, **kwargs)
        return response
    
    def get(self, endpoint: str, **kwargs: Any) -> requests.Response:
        return self.request('GET', endpoint, **kwargs)

    
    def post(self, endpoint: str, **kwargs: Any) -> requests.Response:
        return self.request('POST', endpoint, **kwargs)
    
    def put(self, endpoint: str, **kwargs: Any) -> requests.Response:
        return self.request('PUT', endpoint, **kwargs)

    
    def delete(self, endpoint: str, **kwargs: Any) -> requests.Response:
        return self.request('DELETE', endpoint, **kwargs)