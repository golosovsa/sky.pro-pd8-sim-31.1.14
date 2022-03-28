from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import generics, serializers as rest_serializers
from create_choco.models import Chocolate
from create_choco import views
from create_choco.create_choco_test import test_create_choco
from create_choco import urls as student_urls


class ChocolateSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = Chocolate
        fields = ("price", )


class ChocoViewSet(generics.CreateAPIView):
    queryset = Chocolate.objects.all()
    serializer_class = ChocolateSerializer


views.ChocoCreateView = ChocoViewSet
student_urls.urlpatterns = []


class UseFactoryClassTestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_raises_when_name_incorrect(self):
        with self.assertRaises(
            AssertionError,
            msg=(
                 "Проверьте, что если в ответе на POST запрос по адресу /create_choco/" 
                 "возвращается ответ отличный от ожидаемого, или же не возвращается код 201 (200) то тест падает"
            )
        ):
            test_create_choco(self.client)
