from django.shortcuts import render,redirect
from django.http import Http404
from django.views.generic.base import TemplateView
from .form import *
from django.views.generic import ListView



def home(request):
    product = Product.objects.all()
    return render(request, 'Home.html', {'product':product,})
    
def productList(request):
    try:
        #perform an ORM query to get specific clubs
        product = Product.objects.all()
        
    except Product.DoesNotExist:
        raise Http404("Products not found")
    return render(request, 'ProductList.html', {'product':product,})

def search(request):
    try:
        if request.method == "POST":
            query_name = request.POST.get('name',None)
            if query_name:
                results = Product.objects.filter(name__icontains=query_name)
                return render(request, 'SearchResults.html', {'results':results,})
    except Product.DoesNotExist:
        raise Http404("Product not found")
    return render(request, 'SearchResults.html')


def club(request):
    try:
        if request.method == "POST":
            query_name = request.POST.get('Club',None)
            if query_name:  
                product = Product.objects.filter(category__icontains=query_name)
        
    except Product.DoesNotExist:
        raise Http404("Club not found")
    return render(request, 'ProductListClub.html', {'product':product,})


def clubSet(request):
    try:
        #perform an ORM query to get specific clubs
        product = Product.objects.filter(category__icontains='FullSet') 
        #&& category='HalfSet')
    except Product.DoesNotExist:
        raise Http404("Club not found")
    return render(request, 'ProductListSet.html', {'product':product,})

def accessory(request):
    try:
        #perform an ORM query to get specific clubs
        product = Product.objects.filter(category__icontains='Accessory')
    except Product.DoesNotExist:
        raise Http404("Club not found")
    return render(request, 'ProductListAccess.html', {'product':product,})

def singleProduct(request, id):
    try:
        #perform an ORM query to get specific clubs
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404("Club not found")
    return render(request, 'SingleProduct.html', {'product':product,})


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


