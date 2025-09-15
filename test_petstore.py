import pytest
import time
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
    pet_id = int(time.time())
    payload = {"id": pet_id, "name": "test_pet", "status": "available"}
    create_response = petstore_client.add_pet(payload)
    assert create_response.status_code == 200
    time.sleep(0.3)
    response = petstore_client.get_pet(pet_id)
    assert response.status_code == 200
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
    

def test_delete_existing_pet():
    http_client = HttpClient('https://petstore.swagger.io/v2/')
    petstore_client = PetstoreClient(http_client)
    pet_id = int(time.time())
    payload = {"id": pet_id, "name": "pet_to_delete", "status": "available"}
    assert petstore_client.add_pet(payload).status_code == 200
    time.sleep(0.5)
    response = petstore_client.delete_pet(pet_id)
    if response.status_code == 404:
        time.sleep(0.8)
        response = petstore_client.delete_pet(pet_id)
    assert response.status_code == 200


def test_delete_non_existing_pet():
    http_client = HttpClient('https://petstore.swagger.io/v2/')
    petstore_client = PetstoreClient(http_client)
    response = petstore_client.delete_pet(999999999)
    assert response.status_code == 404