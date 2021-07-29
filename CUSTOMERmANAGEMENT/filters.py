import django_filters
from .models import *
from django_filters import DateFilter, CharFilter


class MyFilter(django_filters.FilterSet):
    Start_Date = DateFilter(field_name='Date_Created', lookup_expr='gte')
    End_Date = DateFilter(field_name='Date_Created', lookup_expr='lte')
    Note = CharFilter(field_name='Note', lookup_expr='icontains')
    class Meta:
        model = ORDER
        fields = '__all__'
        exclude = ['Customer', 'Date_Created', 'Note']