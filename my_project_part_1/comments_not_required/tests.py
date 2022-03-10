from django.test import TestCase
from rest_framework.test import APIClient
from ttools.skyprotests.tests_mixins import ResponseTestsMixin
from comments_not_required.models import Calendar

EVENT_CREATE_URL = '/events/'


class VacationClassTestCase(TestCase, ResponseTestsMixin):

    def setUp(self):
        self.student_app = APIClient()
        self.url = EVENT_CREATE_URL

    def test_url_with_comment_text_works_correct(self):
        response = self.student_app.post(
            self.url,
            data={
                "title": "test title",
                "start_date": "2022-01-10",
                "end_date": "2022-02-10",
                "comment": "best comment ever!",
            }
        )
        self.assertTrue(
            response.status_code in [200, 201],
            f"Проверьте, при POST-запросе на адрес {EVENT_CREATE_URL} в случае, когда поле comment содержит текст то возвращается статус 201 или 200"
        )
        vacation_count = Calendar.objects.all().count()
        self.assertTrue(
            vacation_count == 1,
            f"Проверьте, что при POST-запроса на адрес {EVENT_CREATE_URL}  в случае, когда поле comment содержит текст то создается запись в БД"
        )

        response = self.student_app.patch(
            f"{self.url}1/",
            data={
                "comment": "new_best_comment2",
            }
        )
        self.assertTrue(
            response.data.get("comment") == "",
            f"Проверьте, при PATCH-запросе на адрес {EVENT_CREATE_URL}<id>/ поле comment невозможно изменить"
        )

    def test_url_without_comment_text_works_correct(self):
        response = self.student_app.post(
            self.url,
            data={
                "title": "test title",
                "start_date": "2022-01-10",
                "end_date": "2022-02-10",
                "comment": "",
            }
        )
        self.assertTrue(
            response.status_code in [200, 201],
            f"Проверьте, при POST-запросе на адрес {EVENT_CREATE_URL} в случае, когда поле comment передано, но не содержит текст, то возвращается статус 201 или 200"
        )
        vacation_count = Calendar.objects.all().count()
        self.assertTrue(
            vacation_count == 1,
            f"Проверьте, что при POST-запроса на адрес {EVENT_CREATE_URL}  в случае, когда поле comment передано, но не содержит текст, то создается запись в БД"
        )

    def test_url_without_comment_field_works_correct(self):
        response = self.student_app.post(
            self.url,
            data={
                "title": "test title",
                "start_date": "2022-01-10",
                "end_date": "2022-02-10",
            }
        )
        self.assertTrue(
            response.status_code in [200, 201],
            f"Проверьте, при POST-запросе на адрес {EVENT_CREATE_URL} в случае, когда запрос не содержит поле comment, то возвращается статус 201 или 200"
        )
        vacation_count = Calendar.objects.all().count()
        self.assertTrue(
            vacation_count == 1,
            f"Проверьте, что при POST-запроса на адрес {EVENT_CREATE_URL} в случае, когда запрос не содержит поле comment, то создается запись в БД"
        )
