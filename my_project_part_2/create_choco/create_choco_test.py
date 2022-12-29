import pytest


@pytest.mark.django_db
def test_create_choco(client):
    expected = {
        "name": "Test"
    }

    data = {
        "name": "test",
        "description": "test",
        "price": 100
    }

    response = client.post("/choco_create/", data=data)
    assert response.status_code == 201
    assert response.data == expected
