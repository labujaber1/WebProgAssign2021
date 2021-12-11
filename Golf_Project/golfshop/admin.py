from django.contrib import admin


from .models import Customer, Order,Product,BookFitting,GeneralEnquiry

@admin.register(GeneralEnquiry)
class ClubAdmin(admin.ModelAdmin):
    list_display = ['name','from_email','subject']

@admin.register(Customer)
class ClubAdmin(admin.ModelAdmin):
    # This changes the display of the Pet object in the Admin to a list of attributes
    list_display = ['first_name','last_name', 'gender']

@admin.register(Product)
class ClubAdmin(admin.ModelAdmin):
    # This changes the display of the Pet object in the Admin to a list of attributes
    list_display = ['name', 'category', 'price','quantity']
    list_filter = ('brand','price','stockCondition','quantity')
    search_fields = ['name']

@admin.register(BookFitting)
class ClubAdmin(admin.ModelAdmin):
    # This changes the display of the Pet object in the Admin to a list of attributes
    list_display = ['name', 'fitting_date', 'contact_details']


@admin.register(Order)
class ClubAdmin(admin.ModelAdmin):
    list_display = ['customer','product','orderDate']