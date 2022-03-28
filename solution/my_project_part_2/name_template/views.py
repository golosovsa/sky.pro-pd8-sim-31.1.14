from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from name_template.models import Chocolate
from name_template.serializers import ChocoTemplateSerializer


class CreateChocoTemplate(viewsets.ModelViewSet):
    queryset = Chocolate.objects.all()
    serializer_class = ChocoTemplateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=False)
        if not serializer.is_valid():
            return Response({"error": "This name not allowed"}, status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

