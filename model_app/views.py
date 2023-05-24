from rest_framework.views import APIView
from django.http.response import JsonResponse
from rest_framework import status


class HelloView(APIView):
    def get(self, request):
        return JsonResponse({"message": "Hello World"}, status=status.HTTP_200_OK)