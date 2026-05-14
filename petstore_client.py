from typing import Any, Dict
from requests import Response
from http_client import HttpClient


class PetstoreClient(HttpClient):

    def __init__(self, url: str = 'https://petstore.swagger.io/v2/'):
        super().__init__(url)

    def add_pet(self, pet_data: Dict[str, Any]) -> Response:
        return self.post('pet', json=pet_data)

    def get_pet(self, pet_id: int) -> Response:
        return self.get(f'pet/{pet_id}')

    def update_pet(self, pet_data: Dict[str, Any]) -> Response:
        return self.put('pet', json=pet_data)

    def delete_pet(self, pet_id: int) -> Response:
        return self.delete(f'pet/{pet_id}')

    def find_by_status(self, status: str) -> Response:
        return self.get(f'pet/findByStatus?status={status}')
