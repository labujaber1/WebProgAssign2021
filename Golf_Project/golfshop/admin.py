from django.contrib import admin
from .models import Club, Customer, bookFittingForm,orderForm

from django.urls import path


# Register your models here.
#admin.site.register(Club)
admin.site.register(Customer)
admin.site.register(bookFittingForm)
admin.site.register(orderForm)

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    # This changes the display of the Pet object in the Admin to a list of attributes
    list_display = ['club_name', 'club_type', 'club_price', 'club_stockCondition']


