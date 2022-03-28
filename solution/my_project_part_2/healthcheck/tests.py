from django.test import TestCase
from rest_framework.test import APIClient
from healthcheck.healthcheck_test import test_lifecheck
from healthcheck import urls as student_urls


student_urls.urlpatterns = []


class UseFactoryClassTestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_raises_when_name_incorrect(self):
        with self.assertRaises(
            AssertionError,
            msg=(
                 "Проверьте, что в случае если один из имеющихся эндпоинтов не отвечает на GET запрос " 
                 "то ваш тест падает"
            )
        ):
            for url in ["/lifecheck/", "/readycheck/", "/healthcheck/"]:
                test_lifecheck(self.client, url)
