import factory

from choco.models import Chocolate


class ChocolateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Chocolate

    name = "Choco"
