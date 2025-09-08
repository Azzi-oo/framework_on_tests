from http_client import HttpClient


class PetstoreClient:
    
    def __init__(self, http_client: HttpClient):
        self.http_client = http_client
    
    def add_pet(self, pet_data):
        return self.http_client.post('/pet', data=pet_data)
    
    def get_pet(self, pet_id):
        return self.http_client.get(f'/pet/{pet_id}')
    
    def update_pet(self, pet_data):
        return self.http_client.put('/pet', data=pet_data)
    
    def delete_pet(self, pet_id):
        return self.http_client.delete(f'/pet/{pet_id}')