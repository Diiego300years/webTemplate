import pytest
from api.database.models.items import about_me
from api import create_app


@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


def test_get_about_me_values(client):
    response = client.get('/about_me')
    assert response.status_code == 200
    assert response.json == {
    "code": 1234,
    "description": "I love programming <3 <3 <3",
    "name": "Marcin Buczak",
    "profession": "Programmer"
    }
    assert response.json != False
    assert response.json == about_me


#q: Are you there?
#a: 
