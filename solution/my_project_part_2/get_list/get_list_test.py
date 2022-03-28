import pytest


@pytest.mark.django_db
def test_root_ok(client):
    response = client.get("/get_list/")
    assert response.status_code == 200
