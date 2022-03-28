from django.test import TestCase
import factory
import pytest
from pytest_factoryboy import register
from choco.list_test import test_list_view
from choco.factories import ChocolateFactory
from rest_framework.test import APIClient
from rest_framework import viewsets
# Factories
from choco import views
from choco.models import Chocolate
from choco.serializers import ChocoSerializer


register(ChocolateFactory)


class ChocoViewSet(viewsets.ModelViewSet):
    queryset = Chocolate.objects.all()
    serializer_class = ChocoSerializer


views.ChocoViewSet = ChocoViewSet


class UseFactoryClassTestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        ChocolateFactory.create_batch(6)

    def test_raises_when_name_incorrect(self):
        with self.assertRaises(
            AssertionError,
            msg=(
                 "Проверьте, что если в ответе на запрос по адресу /choco/ в аттрибуте data" 
                 "возвращается 6 объектов, то тест выдает ошибку"
            )
        ):
            test_list_view(self.client)
