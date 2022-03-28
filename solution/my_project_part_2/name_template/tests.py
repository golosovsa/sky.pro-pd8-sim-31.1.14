from django.test import TestCase
from rest_framework.test import APIClient
from name_template.template_test import test_save_choco


class UseFactoryClassTestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_fails_if_name_is_correct_and_code_is_wrong(self):
        with self.assertRaises(
            AssertionError,
            msg=(
                 "Проверьте, что ваш тест падает в случае если на POST-запрос по адресу /chocolate/create cо значением"
                 "поля name: Choco объект не создается и не возвращается код 200"
            )
        ):
            test_save_choco(self.client, "Choco", 422)

    def test_fails_if_name_is_wrong_and_code_is_correct(self):
        with self.assertRaises(
            AssertionError,
            msg=(
                 "Проверьте, что ваш тест падает в случае если на POST-запрос по адресу /chocolate/create cо значением"
                 "поля name: test объект не создается и не возвращается код 422"
            )
        ):
            test_save_choco(self.client, "test", 200)
