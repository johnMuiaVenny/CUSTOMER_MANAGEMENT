from django.shortcuts import render
from .models import *

# Create your views here.

def Home(request):
    Total_Orders = ORDER.objects.all().count()

    return render(request, 'CUSTOMERmANAGEMENT/Home.html', {'Total_Orders':Total_Orders})
