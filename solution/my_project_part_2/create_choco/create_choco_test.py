import pytest


@pytest.mark.django_db
def test_create_choco(client):
    expected_response = {
        "name": "Choco",
    }

    data = {
        "name": "Choco",
        "description": "test description",
        "price": 5.1
    }

    response = client.post("/choco_create/", data=data)
    assert response.status_code == 201
    assert response.data == expected_response
    pass
