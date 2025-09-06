import requests


class HttpClient:
    
    def __init__(self, url: str):
        self.url = url
    
    def request(self, method: str, endpoint: str, data=None) -> requests.Response:
        url = self.url.rstrip('/') + '/' + endpoint.lstrip('/')
        response = requests.request(method, url, json=data)
        return response
    
    def get(self, method: str, endpoint: str, data=None) -> requests.Response:
        return self.request(method, endpoint, data)

    
    def post(self, method: str, endpoint: str, data=None) -> requests.Response:
        return self.request(method, endpoint, data)
    
    def put(self, method: str, endpoint: str, data=None) -> requests.Response:
        return self.request(method, endpoint, data)

    
    def delete(self, method: str, endpoint: str, data=None) -> requests.Response:
        return self.request(method, endpoint, data)