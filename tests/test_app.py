from http import HTTPStatus

from fast_zero.schema import UserPublic


def test_read_root_deve_retornar_OK(client):
    response = client.get('/')  # Act (Ação)

    assert response.status_code == HTTPStatus.OK  # assert (Confirma ação)
    assert response.json() == {'message': 'Olá mundo!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'testeusername',
            'email': 'test@test.com',
            'password': 'password',
        },
    )

    # Retornou o status_code correto?
    assert response.status_code == HTTPStatus.CREATED
    # Validar o UserPublic
    assert response.json() == {
        'username': 'testeusername',
        'email': 'test@test.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')  # Act /Ação

    assert response.status_code == HTTPStatus.OK  # assert (Confirma ação)
    assert response.json() == {'users': []}


def test_read_users_with_user(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()

    response = client.get('/users/')  # Act /Ação

    assert response.status_code == HTTPStatus.OK  # assert (Confirma ação)
    assert response.json() == {'users': [user_schema]}


def test_update_user(client, user, token):
    response = client.put(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'password': '123',
            'username': 'testeusername2',
            'email': 'test@test.com',
            'id': 1,
        },
    )

    assert response.json() == {
        'username': 'testeusername2',
        'email': 'test@test.com',
        'id': 1,
    }


def test_delete_user(client, user, token):
    # print(f'\nID do user no teste: {user.id}')
    response = client.delete(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.json() == {'message': 'User deleted'}


def test_get_token(client, user):
    response = client.post('/token', data={'username': user.email, 'password': user.clean_password})

    token = response.json()

    assert response.status_code == HTTPStatus.OK
    assert token['token_type'] == 'Bearer'
    assert 'access_token' in token
