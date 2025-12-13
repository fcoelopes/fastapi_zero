from http import HTTPStatus

from fastapi import FastAPI

from fastapi_zero.schemas import Message

app = FastAPI(title='FastAPI Zero', version='0.1.0')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá, mundo'}


@app.get('/health', status_code=HTTPStatus.OK, response_model=Message)
def health_check():
    return {'message': 'OK'}
