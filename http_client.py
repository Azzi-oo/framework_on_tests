from typing import Any
import requests


class HttpClient:
    
    def __init__(self, url: str):
        self.url = url
        
    def _request(self, method, endpoint, json=None):
        full_url = f'{self.url}{endpoint}'
        print(f'-> {method} {full_url}')
        
        if json is not None:                                                                                                               
          print(f'    body: {json}')
        
        response = requests.request(method, f'{self.url}{endpoint}', json=json)

        print(f'<- {response.status_code} {response.reason}')
        print(response.text)
        return response
        
    def get(self, endpoint):
        response = self._request('GET', endpoint=endpoint)
        return response
        
        
    def post(self, endpoint, json):
        response = self._request('POST', endpoint=endpoint, json=json)
        return response
        
        
    def put(self, endpoint, json):
        response = self._request('PUT', endpoint=endpoint, json=json)
        return response

        
    def delete(self, endpoint):
        response = self._request('DELETE', endpoint=endpoint)
        return response