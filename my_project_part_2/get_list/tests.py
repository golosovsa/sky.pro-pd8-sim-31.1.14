from django.test import TestCase
from rest_framework.test import APIClient
from get_list.get_list_test import test_root_ok
from get_list import urls as student_urls


student_urls.urlpatterns = []


class UseFactoryClassTestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_raises_when_name_incorrect(self):
        with self.assertRaises(
            AssertionError,
            msg=(
                 "Проверьте, что в случае если GET запрос на адрес /get_list/ " 
                 "не возвращает статус 200 то ваш тест падает"
            )
        ):
            test_root_ok(self.client)
