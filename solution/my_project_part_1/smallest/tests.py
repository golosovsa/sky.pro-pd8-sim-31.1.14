import factory
from smallest.models import SmallPost
from django.test import TestCase
from rest_framework.test import APIClient
from ttools.skyprotests.tests_mixins import ResponseTestsMixin
from django.contrib.auth import get_user_model

User = get_user_model()


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SmallPost

    title = "teststore"
    slug = "testpost"
    text = "teststore"


TOKEN_URL = '/token/'
POST_CREATE_URL = '/smallest/'


class RegisterClassTestCase(TestCase, ResponseTestsMixin):
    @classmethod
    def setUpClass(cls):
        super(RegisterClassTestCase, cls).setUpClass()
        User.objects.create_user(username="skypro_user", password="skypro", first_name="first", last_name="last")

    def setUp(self):
        self.model = User
        self.student_app = APIClient()

    def test_user_works_correct(self):
        user = User.objects.get(username='skypro_user')
        response = self.student_app.post(
                TOKEN_URL,
                {
                 "username": "skypro_user",
                 "password": "skypro"
                },
                format="json"
            )
        token = response.data.get("token", None)
        self.student_app.force_authenticate(user=user, token=token)

        self.url = POST_CREATE_URL
        response = self.student_app.post(
            self.url,
            data={
                "title": "teststore",
                "slug": "testpost",
                "text": "12345"
            }
        )
        self.assertTrue(
            response.status_code in [200, 201],
            "Проверьте, что пользователь может создать пост со значением text больше или равно 5"
        )
        posts_count = SmallPost.objects.all().count()
        self.assertTrue(
            posts_count == 1,
            f"Проверьте, что при POST-запроса на адрес {POST_CREATE_URL} со значением text больше или равно 5 объект создается в БД"
        )

        response = self.student_app.post(
            self.url,
            data={
                "title": "teststore",
                "slug": "testpost",
                "text": "1234"
            }
        )
        self.assertTrue(
            response.status_code in [400],
            f"Проверьте, что пользователь не может создать пост со значением text меньше 5"
        )
        self.assertTrue(
            posts_count == 1,
            f"Проверьте, что при POST-запроса на адрес {POST_CREATE_URL} со значением text меньше 5 объект не создается в БД"
        )

