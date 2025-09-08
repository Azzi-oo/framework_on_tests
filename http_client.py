import requests


class HttpClient:
    
    def __init__(self, url: str):
        self.url = url
    
    def request(self, method: str, endpoint: str, data=None) -> requests.Response:
        url = self.url.rstrip('/') + '/' + endpoint.lstrip('/')
        response = requests.request(method, url, json=data)
        return response
    
    def get(self, endpoint: str) -> requests.Response:
        return self.request('GET', endpoint)

    
    def post(self, endpoint: str, data=None) -> requests.Response:
        return self.request('POST', endpoint, data)
    
    def put(self, endpoint: str, data=None) -> requests.Response:
        return self.request('PUT', endpoint, data)

    
    def delete(self, endpoint: str) -> requests.Response:
        return self.request('DELETE', endpoint)