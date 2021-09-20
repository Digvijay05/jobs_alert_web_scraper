from django.urls import path, include
from .views import api_overview

urlpatterns = [
    path('', api_overview, name='api-overview'),
]