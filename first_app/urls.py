from django.urls.conf import path

from first_app import views

urlpatterns = [
    path("test/celery/task", views.testCeleryTask.as_view()),
    path("", views.DefaultView.as_view())
]
