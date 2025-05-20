from http import HTTPStatus


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
    assert response.json() == {
        'users': [
            {
                'username': 'testeusername',
                'email': 'test@test.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
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


def test_delete_user(client):
    response = client.delete('users/1')

    assert response.json() == {'message': 'User deleted'}
