from http_client import HttpClient


class PetstoreClient:
    
    def __init__(self, http_client: HttpClient):
        self.http_client = http_client
    
    def add_pet(self, pet_data=None):
        if pet_data is None:
            pet_data = {
                "id": 1,
                "name": "test_pet",
                "status": "available"
            }
        return self.http_client.post('POST', '/pet', data=pet_data)
    
    def get_pet(self, pet_id):
        return self.http_client.get('GET', f'/pet/{pet_id}')
    
    def update_pet(self):
        return self.http_client.put('PUT', '/pet')
    
    def delete_pet(self, pet_id):
        return self.http_client.delete('DELETE', f'/pet/{pet_id}')