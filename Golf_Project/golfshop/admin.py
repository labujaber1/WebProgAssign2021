from django.contrib import admin
from .models import Customer,Product,BookFitting,GeneralEnquiry

admin.site.register(GeneralEnquiry)
@admin.register(Customer)
class ClubAdmin(admin.ModelAdmin):
    # This changes the display of the Pet object in the Admin to a list of attributes
    list_display = ['first_name','last_name', 'gender']

@admin.register(Product)
class ClubAdmin(admin.ModelAdmin):
    # This changes the display of the Pet object in the Admin to a list of attributes
    list_display = ['name', 'category', 'price','quantity']


@admin.register(BookFitting)
class ClubAdmin(admin.ModelAdmin):
    # This changes the display of the Pet object in the Admin to a list of attributes
    list_display = ['name', 'fitting_date', 'contact_details']


