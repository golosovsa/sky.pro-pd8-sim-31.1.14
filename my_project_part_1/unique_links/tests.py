from unique_links.models import UniquePost
from django.db.models.fields import CharField, SlugField
from django.test import TestCase
from ttools.skyprotests.tests_mixins import ResponseTestsMixin, DataBaseTestsMixin
from django.contrib.auth import get_user_model

from django.db import models

User = get_user_model()

char_fields = {
    "title": {"max_length": 100},
    "text": {"max_length": 1000},
}

slug_fields = {
    "slug": {"max_length": 20, "unique": True}
}
foreign_key_fields = {
    "author": {"on_delete": models.CASCADE, "model": User}
}

id_field = {
    "id": {"unique": True}
}


def get_model_attributes(*args):
    result = {}
    for arg in args:
        result.update(arg)
    return result


class StoreClassTestCase(TestCase, ResponseTestsMixin, DataBaseTestsMixin):

    def setUp(self):
        self.model = UniquePost

    def test_store_has_expected_fields(self):
        current_fields = {field.name: field for field in self.model._meta.fields}
        expected_fields = get_model_attributes(char_fields, slug_fields, foreign_key_fields, id_field)
        student_attrs_len = len(current_fields)
        expected_attrs_len = len(expected_fields)
        self.assertEqual(
            student_attrs_len,
            expected_attrs_len,
            ("%@ Проверьте, что добавили все необходимые аттрибуты."
            f" Мы насчитали у Вас {student_attrs_len}, тогда как должно быть {expected_attrs_len}"
        ))

        for field_name in expected_fields:
            self.assertIn(
                field_name,
                current_fields,
                f"Проверьте, что добавили в модель поле {field_name}"
            )

        # Checking char_fields
        self.django_field_checker(current_fields, char_fields, CharField)

        # Checking email_fields
        self.django_field_checker(current_fields, slug_fields, SlugField)

        self.django_foreign_key_field_checker(
            current_fields["author"], foreign_key_fields["author"], models.ForeignKey
        )

