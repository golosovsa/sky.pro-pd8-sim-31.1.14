from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class HealthCheckView(APIView):

    def get(self, request):
        return Response({"health_check": "OK"}, status=status.HTTP_200_OK)


class ReadyCheckView(APIView):

    def get(self, request):
        return Response({"ready_check": "OK"}, status=status.HTTP_200_OK)


class LifeCheckView(APIView):

    def get(self, request):
        return Response({"life_check": "OK"}, status=status.HTTP_200_OK)
