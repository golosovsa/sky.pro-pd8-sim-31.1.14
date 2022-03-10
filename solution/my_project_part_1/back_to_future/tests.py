import factory
from back_to_future.models import Vacation, Code
from django.test import TestCase
from rest_framework.test import APIClient
from ttools.skyprotests.tests_mixins import ResponseTestsMixin
from django.contrib.auth import get_user_model

User = get_user_model()


class VacationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Vacation

    date_from = "2022-01-11"
    date_to = "2022-02-11"


class CodeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Code

    code = "main"


VACATION_CREATE_URL = '/back_to_future/'


class VacationClassTestCase(TestCase, ResponseTestsMixin):
    @classmethod
    def setUpClass(cls):
        super(VacationClassTestCase, cls).setUpClass()
        User.objects.create_user(username="skypro_user", password="skypro", first_name="first", last_name="last")
        CodeFactory.create()

    def setUp(self):
        self.model = User
        self.student_app = APIClient()

    def test_user_works_correct(self):
        self.url = VACATION_CREATE_URL
        response = self.student_app.post(
            self.url,
            data={
                "date_from": "2022-01-10",
                "date_to": "2022-02-10",
                "code": "main",
                "user": 1
            }
        )
        self.assertTrue(
            response.status_code in [200, 201],
            f"Проверьте, при POST-запросе на адрес {VACATION_CREATE_URL} при правильном значении поля code возвращается статус 201 или 200"
        )
        vacation_count = Vacation.objects.all().count()
        self.assertTrue(
            vacation_count == 1,
            f"Проверьте, что при POST-запроса на адрес {VACATION_CREATE_URL} c допустимым значением code создается запись в БД"
        )

        response = self.student_app.post(
            self.url,
            data={
                "date_from": "2022-01-10",
                "date_to": "2022-02-10",
                "code": "wrong_code",
                "user": 1
            }
        )
        self.assertTrue(
            response.status_code in [400],
             f"Проверьте, что при POST-запроса на адрес {VACATION_CREATE_URL} возвращается код 400 если значение поле code отсутствует в базе"
        )
        self.assertTrue(
            vacation_count == 1,
            f"Проверьте, что при POST-запроса на адрес {VACATION_CREATE_URL} если поле code отсутствует в БД то запись об отпуске не создается"
        )

