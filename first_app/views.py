from rest_framework import status
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.views import APIView

from celery_app import tasks


class DefaultView(APIView):

    def get(self, request):
        return Response(status=status.HTTP_200_OK)


class testCeleryTask(APIView):

    def get(self, request):
        tasks.check_celery_task.delay()
        return JsonResponse(data={"message": "task triggered"}, status=status.HTTP_200_OK)


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def schedule_task_test(request):
    if request.method == 'GET':
        # Extract necessary data from the request
        # Example: task_parameters = request.POST.get('task_parameters')

        # Schedule the task
        tasks.scheduel_task.apply_async(args=("Hello", "World"), countdown=10)

        return JsonResponse({'message': 'Task scheduled successfully'})
