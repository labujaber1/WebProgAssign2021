from .models import Product
import django_filters



class SearchList(django_filters.FilterSet):
    '''  minPrice = django_filters.NumberFilter(name="price", lookup_type='gte')
        maxPrice = django_filters.NumberFilter(name="price", lookup_type='lt')
    ,'minPrice','maxPrice'
    '''
    class Meta:
        model = Product
        fields = ['brand','gender','size','gripDirection']
        #minPice= django_filters.DecimalField(max_digits=7, decimal_places=2)
        #maxPrice= django_filters.DecimalField(max_digits=7, decimal_places=2)



