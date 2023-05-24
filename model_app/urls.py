from django.urls import path, include
from model_app.views import HelloView

urlpatterns = [
    path('test_model_app', HelloView.as_view()),
]