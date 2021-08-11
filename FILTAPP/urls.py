from django.urls import path
from .views import *

app_name='FILTAPP'

urlpatterns = [
    path('', Test, name='Test'),
]