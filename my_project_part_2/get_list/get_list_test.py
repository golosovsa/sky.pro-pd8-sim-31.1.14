import pytest
from django.test import Client


@pytest.mark.django_db
def test_root_ok(client: Client):
    response = client.get('/get_list/')

    assert response.status_code == 200
