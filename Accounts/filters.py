from django_filters import filters,CharFilter,DateFilter
from Accounts.models import Order
import django_filters

#Normally filter are used to search in 
class OrderFilter(django_filters.FilterSet):
    status = CharFilter(field_name='status',lookup_expr='icontains')

    class Meta:
        model = Order
        fields =['date']
        excludes = ['date','customer']