from rest_framework import serializers
from smallest.models import SmallPost


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = SmallPost
        fields = ("title", "slug", "text", "author")
        read_only_fields = ("author", )
