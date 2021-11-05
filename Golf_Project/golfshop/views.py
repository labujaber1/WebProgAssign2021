from django.shortcuts import render
from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .form import *
from django.http import HttpResponse

#def golfshop(request):
    #return render(request, 'home.html')

def home(request):
    clubs=Club.objects.all()
    context={'clubs':clubs}
    return render(request, "home.html", context)
    
 

