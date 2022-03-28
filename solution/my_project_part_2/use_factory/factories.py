import factory

from use_factory.models import Skill


class SkillFactory(factory.django.DjangoModelFactory):
    name = "Skill 1"

    class Meta:
        model = Skill


