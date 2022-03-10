from rest_framework import viewsets, permissions
from smallest.serializers import PostSerializer
from smallest.models import SmallPost


class PostViewSet(viewsets.ModelViewSet):
    queryset = SmallPost.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)

