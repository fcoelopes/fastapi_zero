from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retornar_ola_mundo():
    client = TestClient(app)
    response = client.get('/')
    # assert response.status_code == 200
    assert response.json() == {'message': 'Olá, mundo'}
    assert response.status_code == HTTPStatus.OK


def test_create_user_deve_criar_e_retornar_usuario():
    client = TestClient(app)
    response = client.post(
        '/users/',
        json={
            'username': 'fcoed',
            'email': 'fcoed1@example.com',
            'password': 'strongpassword123',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'fcoed',
        'email': 'fcoed1@example.com',
        'id': 1,
    }
