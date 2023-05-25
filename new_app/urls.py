from django.urls import path
from new_app import views

urlpatterns = [
    path('test/celery', views.testCeleryTask.as_view()),
]