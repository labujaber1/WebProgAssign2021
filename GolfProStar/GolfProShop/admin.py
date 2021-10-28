from django.contrib import admin
from django.urls import path
from .models import ProductID


# Register your models here.
@admin.register(ProductID)
class ProductAdmin(admin.ModelAdmin):
    # This changes the display of the ProductID object in the Admin to a list of attributes
   
    list_display = ['productName','productPrice','clubType','size','grip']


from GolfProShop import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    #pet_detail is name of html page
    #path('appname/<int:pet_id>/', views.pet_detail,
    
    #name="pet_detail"),
] 