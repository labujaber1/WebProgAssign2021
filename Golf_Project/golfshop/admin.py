from django.contrib import admin
from .models import Accessories, Customer,Club,BookFitting,GeneralEnquiry, SetOfClubs

admin.site.register(GeneralEnquiry)
@admin.register(Customer)
class ClubAdmin(admin.ModelAdmin):
    # This changes the display of the Pet object in the Admin to a list of attributes
    list_display = ['first_name','last_name', 'gender']

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    # This changes the display of the Pet object in the Admin to a list of attributes
    list_display = ['club_name', 'club_type', 'club_price','quantity']

@admin.register(Accessories)
class ClubAdmin(admin.ModelAdmin):
    # This changes the display of the Pet object in the Admin to a list of attributes
    list_display = ['access_name','access_price','quantity']

@admin.register(SetOfClubs)
class ClubAdmin(admin.ModelAdmin):
    # This changes the display of the Pet object in the Admin to a list of attributes
    list_display = ['clubSet_name','clubSet_price','quantity']

@admin.register(BookFitting)
class ClubAdmin(admin.ModelAdmin):
    # This changes the display of the Pet object in the Admin to a list of attributes
    list_display = ['name', 'fitting_date', 'contact_details']


