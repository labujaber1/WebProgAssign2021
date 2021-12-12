from .models import Product
import django_filters



class SearchList(django_filters.FilterSet):
    price = django_filters.NumberFilter()
    minPrice = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    maxPrice = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
   
    class Meta:
        model = Product
        fields = ['brand','gender','size','gripDirection','price']
        


