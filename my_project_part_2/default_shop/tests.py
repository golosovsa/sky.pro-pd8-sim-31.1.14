from django.test import TestCase
from default_shop import factories
import factory


class FactoryClassTestCase(TestCase):

    def test_url_with_comment_text_works_correct(self):
        student_factory = getattr(factories, "StoreFactory")
        self.assertTrue(
            factory,
            "Проверьте что класс StoreFactory определен в модуле."
        )

        is_factory_django_model_factory = issubclass(student_factory, factory.django.DjangoModelFactory)
        self.assertTrue(
            is_factory_django_model_factory,
            "Проверьте, что класс StoreFactory унаследован от класса DjangoModelFactory"
        )
        attrs = {
            "store_info": factories.DEFAULT_STORE_INFO,
            "store_id": factories. DEFAULT_STORE_SAP,
            "lat": factories.DEFAULT_STORE_LAT,
            "lng": factories.DEFAULT_STORE_LNG
        }
        for key, value in attrs.items():
            self.assertTrue(
                getattr(student_factory, key, None),
                f"Проверьте, что аттрибут {key} определен в классе StoreFactory"
            )
            self.assertTrue(
                getattr(student_factory, key, None) == attrs.get(key),
                f"Проверьте, что аттрибуту {key} класса StoreFactory присвоена соответствующая константа"
            )


