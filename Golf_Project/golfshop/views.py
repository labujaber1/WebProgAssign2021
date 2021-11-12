from django.shortcuts import render,redirect
from django.http import Http404
from .form import *




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
    if request.user.is_authenticated:
        return redirect('home') 
    else: 
        form=customerRegisterForm()
        customerform=customerRegisterForm()
        if request.method=='POST':
            form=customerRegisterForm(request.POST)
            customerform=customerRegisterForm(request.POST)
            if form.is_valid() and customerform.is_valid():
                user=form.save()
                customer=customerform.save(commit=False)
                customer.user=user 
                customer.save()
                return redirect('/')
        context={
            'form':form,
            'customerform':customerform,
        }
        return render(request,"/RegisterCustomer.html",context)
 