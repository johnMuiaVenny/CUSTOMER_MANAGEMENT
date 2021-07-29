import django_filters
from .models import *


class MyFilter(django_filters.FilterSet):
    class Meta:
        model = ORDER
        fields = '__all__'
        exclude = ['Customer']