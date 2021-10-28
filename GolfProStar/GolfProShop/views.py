from django.shortcuts import render
#from django.http import Http404
from .models import ProductID

# Create your views here.
def home(request):
    products=ProductID.objects.all()
    return render(request, "home.html", {'products':products,})

