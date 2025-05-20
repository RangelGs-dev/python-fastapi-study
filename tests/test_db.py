from fast_zero.models import User


def test_create_user():
    user = User(username='Rangel', email='rangelgs17@gmail.com', password='minhasenha')

    assert user.username == 'Rangel'
