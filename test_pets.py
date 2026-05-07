import requests
from http_client import HttpClient


pet = {
  "id": 900,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "lobby",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

client = HttpClient('https://petstore.swagger.io/v2')

client.post('/pet', json=pet)

client.get('/pet/900')

pet['name'] = 'buldog'

client.put('/pet', json=pet)

client.get('/pet/900')

client.delete('/pet/900')

client.get('/pet/900')