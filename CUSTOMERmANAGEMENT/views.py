from django.shortcuts import render
from .models import *
from .filters import *

# Create your views here.

def Home(request):
    Total_Orders = ORDER.objects.all().count()

    Delivered = ORDER.objects.filter(Status='Delivered').count()

    customers = CUSTOMER.objects.all()

    return render(request, 'CUSTOMERmANAGEMENT/Home.html', {'Total_Orders':Total_Orders, 'Delivered':Delivered, 'customers':customers})



#Filter by use of form fields.
def FilterOrders(request, id):
    customer = CUSTOMER.objects.get(pk=id)
    order = customer.order_set.all()

    myFilter = MyFilter(request.GET, queryset=order)
    order = myFilter.qs

    return render(request, 'CUSTOMERmANAGEMENT/FilterOrders.html', {'myFilter':myFilter, 'customer':customer, 'order':order})

