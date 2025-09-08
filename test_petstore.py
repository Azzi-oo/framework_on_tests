import pytest
from http_client import HttpClient
from petstore_client import PetstoreClient


def test_add_pet():
    http_client = HttpClient('https://petstore.swagger.io/v2/')
    petstore_client = PetstoreClient(http_client)
    payload = {"id": 1, "name": "test_pet", "status": "available"}
    response = petstore_client.add_pet(payload)
    assert response.status_code == 200
    body = response.json()
    assert body.get('id') == 1
    assert body.get('name') == 'test_pet'
    


def test_get_pet():
    http_client = HttpClient('https://petstore.swagger.io/v2/')
    petstore_client = PetstoreClient(http_client)
    import time
    pet_id = int(time.time())
    payload = {"id": pet_id, "name": "test_pet", "status": "available"}
    create_response = petstore_client.add_pet(payload)
    assert create_response.status_code == 200
    import time as _t
    response = None
    for _ in range(6):  # до ~3 секунд ожидания
        response = petstore_client.get_pet(pet_id)
        if response.status_code == 200:
            break
        _t.sleep(0.5)
    assert response is not None and response.status_code == 200
    body = response.json()
    assert body.get('id') == pet_id
    assert body.get('name') == 'test_pet'


def test_update_pet():
    http_client = HttpClient('https://petstore.swagger.io/v2/')
    petstore_client = PetstoreClient(http_client)
    payload = {"id": 1, "name": "updated_test_pet", "status": "sold"}
    response = petstore_client.update_pet(payload)
    assert response.status_code == 200
    body = response.json()
    assert body.get('name') == 'updated_test_pet'
    

def test_delete_pet():
    http_client = HttpClient('https://petstore.swagger.io/v2/')
    petstore_client = PetstoreClient(http_client)
    response = petstore_client.delete_pet(1)
    assert response.status_code in [200, 404]