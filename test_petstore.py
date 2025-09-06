from http_client import HttpClient
from petstore_client import PetstoreClient


def test_add_pet():
    http_client = HttpClient('https://petstore.swagger.io/v2/')
    petstore_client = PetstoreClient(http_client)
    response = petstore_client.add_pet()
    assert response.status_code == 200
    


def test_get_pet():
    http_client = HttpClient('https://petstore.swagger.io/v2/')
    petstore_client = PetstoreClient(http_client)
    response = petstore_client.get_pet(1)
    assert response.status_code in [200, 404]


def test_update_pet():
    http_client = HttpClient('https://petstore.swagger.io/v2/')
    petstore_client = PetstoreClient(http_client)
    response = petstore_client.update_pet()
    assert response.status_code == 200
    
    


def test_delete_pet():
    pass