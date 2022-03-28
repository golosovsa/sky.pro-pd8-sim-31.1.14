import pytest


@pytest.mark.django_db
def test_create_vacancy(skill):
    assert skill.name == "Skill 1"