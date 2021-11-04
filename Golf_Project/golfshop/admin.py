from django.contrib import admin
from .models import Club, Customer, bookFittingForm,orderForm

# Register your models here.
admin.site.register(Club)
admin.site.register(Customer)
admin.site.register(bookFittingForm)
admin.site.register(orderForm)

