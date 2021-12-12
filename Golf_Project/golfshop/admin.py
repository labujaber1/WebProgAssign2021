from django.contrib import admin
from .models import *

admin.site.site_header = "GolfPro Website"

@admin.register(GeneralEnquiry)
class ClubAdmin(admin.ModelAdmin):
    list_display = ['name','from_email','subject']

@admin.register(OrderRequest)
class ClubAdmin(admin.ModelAdmin):
    list_diplay = ['customer', 'productName', 'productID', 'dateOfOrder']
    list_filter = ('customer', 'productName', 'dateOfOrder')
    search_fields = ['customer']
    

@admin.register(Customer)
class ClubAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name', 'gender']

@admin.register(Product)
class ClubAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price','quantity']
    list_filter = ('brand','price','stockCondition','quantity')
    search_fields = ['name']

@admin.register(BookFitting)
class ClubAdmin(admin.ModelAdmin):
    list_display = ['name', 'fitting_date', 'contact_details']

