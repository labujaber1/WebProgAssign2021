from django.shortcuts import render,redirect
from django.http import Http404
from django.views.generic.base import TemplateView
from .form import *
from django.views.generic import ListView



def home(request):
    club=Club.objects.all()
    return render(request, 'Home.html', {'club':club,})
    
def productListClubs(request):
    try:
        #perform an ORM query to get specific clubs
        club = Club.objects.all()
        #clubSet = SetOfClubs.objects.all()
        #access = Accessories.objects.all()
    except Club.DoesNotExist:
        raise Http404("Products not found")
    return render(request, 'ProductListClubs.html', {'club':club,})

def productListClubSet(request):
    try:
        #perform an ORM query to get specific clubs
        #club = Club.objects.all()
        clubSet = SetOfClubs.objects.all()
        #access = Accessories.objects.all()
    except Club.DoesNotExist:
        raise Http404("Products not found")
    return render(request, 'ProductListClubSet.html', {'clubSet':clubSet,})

def productListAccess(request):
    try:
        #perform an ORM query to get specific clubs
        #club = Club.objects.all()
        #clubSet = SetOfClubs.objects.all()
        access = Accessories.objects.all()
    except Club.DoesNotExist:
        raise Http404("Products not found")
    return render(request, 'ProductListAccess.html', {'access':access,})

""" def singleProduct(request, id):
    try:
        if(request.method== 'club.id'):
            #perform an ORM query to get specific clubs
            club = Club.objects.get(id=id)
            return render(request, 'SingleProduct.html', {'club':club,})
        if(request.method== 'clubSet.id'):
            clubSet = SetOfClubs.objects.get(id=id)
            return render(request, 'SingleClubSet.html', {'clubSet':clubSet,})
        if(request.method== 'access.id'):
            access = Accessories.objects.get(id=id)
            return render(request, 'SingleAccess.html', {'access':access,})
    except Club.DoesNotExist:
        raise Http404("Club not found")
    return render(request, 'Home.html',) """

def singleProduct(request, id):
    try:
        #perform an ORM query to get specific clubs
        club = Club.objects.get(id=id)
    except Club.DoesNotExist:
        raise Http404("Club not found")
    return render(request, 'SingleProduct.html', {'club':club,})

def setOfProducts(request,id):
    try:
        clubSet = SetOfClubs.objects.get(id=id)
    except Club.DoesNotExist:
        raise Http404("Set of clubs not found")
    return render(request, 'SetOfProducts.html', {'clubSet':clubSet,})

def accessProducts(request,id):
    try:
        access = Accessories.objects.get(id=id)
    except Club.DoesNotExist:
        raise Http404("Accessories not found")
    return render(request, 'SingleAccess.html', {'access':access,})



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

