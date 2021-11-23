"""GolfProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from typing import ValuesView
from django.contrib import admin
from django.urls import path

import golfshop.views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', golfshop.views.home, name="Home"),
    path('ProductList/', golfshop.views.productList, name="ProductList"),
    path('ProductListClub/', golfshop.views.club, name="ProductListClub"),
    path('ProductListSet/', golfshop.views.clubSet, name="ProductListSet"),
    path('ProductListAccess/', golfshop.views.accessory, name="ProductListAccess"),
    
    path('SingleProduct/<int:id>/', golfshop.views.singleProduct, name="SingleProduct"),
    path('SearchResults/', golfshop.views.search, name="SearchResults"),
  
    path('RegisterCustomer',golfshop.views.registerCustomer, name="RegisterCustomer"),
    path('GeneralEnquiry',golfshop.views.generalEnquiry, name="GeneralEnquiry"),
    path('BookFitting',golfshop.views.bookFitting, name="BookFitting"),
    

]+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root = 
    settings.MEDIA_ROOT)

