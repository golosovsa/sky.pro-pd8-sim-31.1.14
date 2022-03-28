from django.test import TestCase
from default_shop import factories
import factory
import pytest
from pytest_factoryboy import register
from use_factory.factory_test import test_create_vacancy
from use_factory.factories import SkillFactory

# Factories
register(SkillFactory)


class Skill:
    name = "Skill 2"


class UseFactoryClassTestCase(TestCase):
    def test_raises_when_name_incorrect(self):
        with self.assertRaises(
            AssertionError,
            msg=("проверьте, что если передать тесту значение поля 'name' "
                 "отличное от 'Skill 1' то тест выбрасывает ошибку")
        ):
            test_create_vacancy(Skill)


