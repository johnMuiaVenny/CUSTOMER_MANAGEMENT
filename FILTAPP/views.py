from django.shortcuts import render
from .models import *
from .filters import *

# Create your views here.

def Test(request):
    test = TEST.objects.all()
    myfilt = Flt(request.GET, queryset=test)
    test=myfilt.qs
    return render(request, 'FILTAPP/Test.html', {'test':test, 'myfilt':myfilt})
