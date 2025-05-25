from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='Rangel',
        email='rangelgs17@gmail.com',
        password='minhasenha',
    )

    session.add(user)
    session.commit()

    result = session.scalar(select(User).where(User.email == 'rangelgs17@gmail.com'))

    assert result.username == 'Rangel'
