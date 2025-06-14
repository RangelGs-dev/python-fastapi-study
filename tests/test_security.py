from http import HTTPStatus

from jwt import decode

from fast_zero.security import ALGORITHM, SECRET_KEY, create_access_token


def test_jwt():
    data_payload = {'sub': 'teste@test.com.br'}

    token = create_access_token(data_payload)

    result = decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    assert result['sub'] == data_payload['sub']
    assert result['exp']


def test_jwt_invalid_token(client):
    response = client.delete('users/1', headers={'Authorization': 'Bearer token-invalid'})

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}
