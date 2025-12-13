from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retornar_ola_mundo():
    client = TestClient(app)
    response = client.get('/')
    # assert response.status_code == 200
    assert response.json() == {'message': 'Olá, mundo'}


def test_health_deve_retornar_ok():
    client = TestClient(app)
    response = client.get('/health')
    # assert response.status_code == 200
    assert response.json() == {'message': 'OK'}
