from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from celery_app import tasks


class DefaultView(APIView):

    def get(self, request):
        return Response(status=status.HTTP_200_OK)


class testCeleryTask(APIView):

    def get(self, request):
        tasks.check_celery_task.delay()
        return Response(data={"message": "task triggered"}, status=status.HTTP_200_OK)
