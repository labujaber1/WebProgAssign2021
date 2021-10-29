from django.contrib import admin
from .models import Club, Club_set, Customer, bookFittingForm,orderForm

# Register your models here.
admin.site.register(Club)
admin.site.register(Club_set)
admin.site.register(Customer)
admin.site.register(bookFittingForm)
admin.site.register(orderForm)

