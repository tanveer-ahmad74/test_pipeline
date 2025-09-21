from django.urls import path
from .views import test_api, cricket_report

urlpatterns = [
    path('api/test/', test_api, name='test-api'),
    path('api/cricket/', cricket_report, name='cricket-report'),
]
