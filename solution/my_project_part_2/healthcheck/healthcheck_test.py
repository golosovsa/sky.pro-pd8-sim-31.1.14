import pytest


@pytest.mark.parametrize("url", ["/lifecheck/", "/readycheck/", "/healthcheck/"])
def test_lifecheck(client, url):
    response = client.get(url)

    assert response.status_code == 200
