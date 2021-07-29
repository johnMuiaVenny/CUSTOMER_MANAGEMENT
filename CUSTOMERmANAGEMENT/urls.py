from django.urls import path
from . import views
from .views import *

app_name='CUSTOMERmANAGEMENT'

urlpatterns = [
    path('', Home, name='Home'),
    path('<int:id>', FilterOrders, name='FilterOrders'),
]