from fastapi.testclient import TestClient
from fastapi import status
from main import app

client=TestClient(app=app)

def test_get():
    response = client.get('/')
    assert response.status_code == status.HTTP_200_OK
    

# def test_post():
#     response = client.post('/',json={"coin_name":"BTC"})
#     assert response.status_code == status.HTTP_201_CREATED
#     assert response.json() == {"coin_name":"BTC"}
