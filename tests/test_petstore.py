from pydoc import cli
import random
import pytest

from petstore_client import PetstoreClient


@pytest.fixture()
def client():
    return PetstoreClient()


@pytest.fixture
def pet_id():
    return random.randint(10**6, 10**9)


@pytest.fixture
def pet_payload(pet_id):
    return {
        "id": pet_id,
        "category": {"id": 1, "name": "dogs"},
        "name": "lobby",
        "photoUrls": ["https://example.com/lobby.jpg"],
        "tags": [{"id": 1, "name": "friendly"}],
        "status": "available",
    }
    

@pytest.fixture
def created_pet(client, pet_payload):
    response = client.add_pet(pet_payload)
    assert response.status_code == 200
    yield pet_payload
    client.delete_pet(pet_payload["id"])


class TestPetstoreClient:

    def test_add_pet(self, client, pet_payload):
        response = client.add_pet(pet_payload)
        assert response.status_code == 200
        body = response.json()
        assert body["id"] == pet_payload["id"]
        assert body["name"] == pet_payload["name"]
        assert body["status"] == "available"
        
        client.delete_pet(pet_payload["id"])
        
    def test_get_pet_returns_created_pet(self, client, created_pet):
        response = client.get_pet(created_pet["id"])
        
        assert response.status_code == 200
        body = response.json()
        assert body["id"] == created_pet["id"]
        assert body["name"] == created_pet["name"]
        
    def test_update_pet_changes_fields(self, client, created_pet):
        created_pet["name"] = "buldog"
        created_pet["status"] = "sold"
        
        response = client.update_pet(created_pet)
        
        assert response.status_code == 200
        body = response.json()
        assert body["name"] == "buldog"
        assert body["status"] == "sold"
        
        fetched = client.get_pet(created_pet["id"]).json()
        assert fetched["name"] == "buldog"
        assert fetched["status"] == "sold"
        
    def test_delete_pet_removes_it(self, client, pet_payload):
        client.add_pet(pet_payload)
        
        response = client.delete_pet(pet_payload["id"])
        assert response.status_code == 200
        
        not_found = client.get_pet(pet_payload["id"])
        assert not_found.status_code == 404
        
    def test_get_missing_pet_returns_404(self, client, pet_id):
        response = client.get_pet(pet_id)
        assert response.status_code == 404