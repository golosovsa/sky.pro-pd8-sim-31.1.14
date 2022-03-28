from default_shop.models import Store

import factory

DEFAULT_STORE_INFO = "Test_store"
DEFAULT_STORE_LAT = 55.8227147
DEFAULT_STORE_LNG = 49.1447822
DEFAULT_STORE_SAP = "G101"


class StoreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Store

    store_info = DEFAULT_STORE_INFO
    # TODO допишите ваш код здесь
