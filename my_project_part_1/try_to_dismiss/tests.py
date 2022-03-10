from django.test import TestCase
from rest_framework.test import APIClient
from ttools.skyprotests.tests_mixins import ResponseTestsMixin
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
User = get_user_model()


CREATE_RESOURCE = '/resources/'


class RegisterClassTestCase(TestCase, ResponseTestsMixin):
    @classmethod
    def setUpClass(cls):
        super(RegisterClassTestCase, cls).setUpClass()

    def setUp(self):
        self.student_app = APIClient()
        (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")

    def test_works_correct_with_wrong_dismiss_date(self):
        wrong_dismiss_date = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
        response = self.student_app.post(
                CREATE_RESOURCE,
                {
                 "grade": 4,
                 "name": "Сергей",
                 "position": "разработчик",
                 "daily_hours": 8,
                 "hire_date": "2022-03-10",
                 "dismiss_date": wrong_dismiss_date
                },
                format="json"
            )
        self.assertTrue(
            response.status_code in [400],
            f"Проверьте, при POST-запросе на адрес {CREATE_RESOURCE} с недопустимым значением поля dismiss_date (раньше текущей даты) возвращается статус 201 (200)"
        )

    def test_works_correct_with_today_dismiss_date(self):
        wrong_dismiss_date = datetime.today().strftime("%Y-%m-%d")
        response = self.student_app.post(
                CREATE_RESOURCE,
                {
                 "grade": 4,
                 "name": "Сергей",
                 "position": "разработчик",
                 "daily_hours": 8,
                 "hire_date": "2022-03-10",
                 "dismiss_date": wrong_dismiss_date
                },
                format="json"
            )
        self.assertTrue(
            response.status_code in [200, 201],
            f"Проверьте, при POST-запросе на адрес {CREATE_RESOURCE} с допустимым значением поля dismiss_date возвращается статус 201 (200)"
        )

    def test_works_correct_with_right_dismiss_date(self):
        wrong_dismiss_date = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")
        response = self.student_app.post(
                CREATE_RESOURCE,
                {
                 "grade": 4,
                 "name": "Сергей",
                 "position": "разработчик",
                 "daily_hours": 8,
                 "hire_date": "2022-03-10",
                 "dismiss_date": wrong_dismiss_date
                },
                format="json"
            )
        self.assertTrue(
            response.status_code in [200, 201],
            f"Проверьте, при POST-запросе на адрес {CREATE_RESOURCE} с допустимым значением поля dismiss_date возвращается статус 201 (200)"
        )
