from django.urls import path
from .views import test_api

urlpatterns = [
    path('api/test/', test_api, name='test-api'),
]
