import django_filters
from .models import *

class Flt(django_filters.FilterSet):
    class Meta:
        model = TEST
        fields = '__all__'