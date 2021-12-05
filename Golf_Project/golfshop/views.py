from django.http.response import BadHeaderError, HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.http import Http404
from .models import Product
from .form import *
from .filters import *



def home(request):
    product = Product.objects.all()
    return render(request, 'Home.html', {'product':product,})

#return all products in card form    
def productList(request):
    try:
        #perform an ORM query to get specific clubs
        product_list = Product.objects.all().order_by("name")
        filter = SearchList(request.GET, queryset=product_list)

    except Product.DoesNotExist:
        raise Http404("Products not found")
    return render(request, 'ProductList.html', {'filter':filter,})


#return all single club products
def club(request):
    try:
        #queryset = Product.objects.filter(category__icontains='Club')  
        query_set = Product.objects.filter(category__startswith='C').order_by("type")
        filter = SearchList(request.GET, queryset=query_set)
    except Product.DoesNotExist:
        raise Http404("Club not found")
    return render(request, 'ProductListClub.html', {'filter':filter,})

#return all set of clubs products
def clubSet(request):
    try:
        queryset = Product.objects.filter(category__startswith='S').order_by("name") 
    except Product.DoesNotExist:
        raise Http404("Club set not found")
    return render(request, 'ProductListSet.html', {'product':queryset,})

#return all accessory products
def accessory(request):
    try:
        queryset = Product.objects.filter(category__startswith='A').order_by("name")
        #queryprice= Product.objects.filter(price__range=(min_price,max_price)).order_by("name")
    except Product.DoesNotExist:
        raise Http404("Club not found")
    return render(request, 'ProductListAccess.html', {'product':queryset,})

#return details of a single club search
def singleProduct(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404("Club not found")
    return render(request, 'SingleProduct.html', {'product':product,})

#register new customer
def registerCustomer(request):
    form=customerRegisterForm()
    if(request.method=='POST'):
        form=customerRegisterForm(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('/')
        
    return render(request, 'RegisterCustomer.html', {'RegisterCustomer': form})

#customer issues an appointment to get a fitting for a club
def bookFitting(request):
    form=customerFittingForm()
    if(request.method=='POST'):
        form=customerFittingForm(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('/')
        
    return render(request, 'BookFitting.html', {'BookFitting': form})

#customer general enquiry form check console for results
def generalEnquiry(request):
    if request.method=='GET':
        form=generalEnquiriesForm()
    else:
        form=generalEnquiriesForm(request.POST,request.FILES)
        if(form.is_valid()):
            subject = "Customer enquiry"
            body ={
            'name': form.cleaned_data['name'],
            'from_email': form.cleaned_data['from_email'],
            'phone_number': form.cleaned_data['phone_number'],
            'enquiry': form.cleaned_data['enquiry'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject,message,'admin@example.com',['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('Success')
    form= generalEnquiriesForm()   
    return render(request, 'GeneralEnquiry.html', {'form': form})

def successEmail(request):
    return HttpResponse('Thankyou for your email')
    #return render(request,'Success.html')

def placeOrder(request):
    customer= Customer.objects.all()
    form=createorderform()
    if(request.method=='POST'):
        form=createorderform(request.POST,instance=customer)
        if(form.is_valid()):
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,"PlaceOrder.html",context)

#single search by product name in nav bar
def search(request):
    try:
        if request.method == "GET":
            query_name = request.GET.get('name',None)
            if query_name:
                results = Product.objects.filter(name__startswith=query_name).order_by("price")
                return render(request, 'SearchResults.html', {'results':results,})
    except Product.DoesNotExist:
        raise Http404("Product not found")
    return render(request, 'SearchResults.html')

#dispays form in advancedSearch.html to search using different fields
#called from urls
def advSearch(request):
    product_list = Product.objects.all()
    #.order_by("name")
    #SearchList is a filter from filters.py
    filter = SearchList(request.GET, queryset=product_list)
    return render(request, 'AdvancedSearch.html', {'filter': filter})



