import json

from celery.result import AsyncResult
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from celery_app import tasks
from mcelery import app


class testCeleryTask(APIView):

    def get(self, request):
        task_id = tasks.scheduel_task.delay(10,20)
        print("--------------->", task_id)
        return Response(data={"message": "task triggered","task_id": task_id}, status=status.HTTP_200_OK)

    def put(self, request):
        task_id = request.data.get('task_id')
        result = AsyncResult(task_id, app=app)
        task_info = {
            'Status': str(result.status),
            'Task Info': result.info
        }
        return Response(data={'Task Info': task_info}, status=status.HTTP_200_OK)