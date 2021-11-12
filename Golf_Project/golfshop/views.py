from django.shortcuts import render,redirect
from django.http import Http404
from django.views.generic.base import TemplateView
from .form import *
from django.views.generic import ListView



def home(request):
    club=Club.objects.all()
    return render(request, 'Home.html', {'club':club,})
    
def productList(request):
    try:
        #perform an ORM query to get specific clubs
        club = Club.objects.all()
        
    except Club.DoesNotExist:
        raise Http404("Clubs not found")
    return render(request, 'ProductList.html', {'club':club,})

def singleProduct(request, id):
    try:
        #perform an ORM query to get specific clubs
        club = Club.objects.get(id=id)
        
    except Club.DoesNotExist:
        raise Http404("Club not found")
    return render(request, 'SingleProduct.html', {'club':club,})

def registerCustomer(request):
    form=customerRegisterForm()
    if(request.method=='POST'):
        form=customerRegisterForm(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('/')
        
    return render(request, 'RegisterCustomer.html', {'RegisterCustomer': form})

def bookFitting(request):
    form=customerFittingForm()
    if(request.method=='POST'):
        form=customerFittingForm(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('/')
        
    return render(request, 'BookFitting.html', {'BookFitting': form})
####
def generalEnquiry(request):
    form=generalEnquiriesForm()
    if(request.method=='POST'):
        form=generalEnquiriesForm(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('/')
       
    return render(request, 'GeneralEnquiry.html', {'GeneralEnquiry': form})

