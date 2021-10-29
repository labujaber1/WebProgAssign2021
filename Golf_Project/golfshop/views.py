from django.shortcuts import render
from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .forms import *
from django.http import HttpResponse

#def golfshop(request):
    #return render(request, 'golfshop_home.html')

def home(request):
    products = Club.objects.all()
    context = {
        'products':products
    }
    return render(request,'home.html',context)
 
def placeOrder(request,i):
    customer= Customer.objects.get(id=i)
    form=createorderform(instance=customer)
    if(request.method=='POST'):
        form=createorderform(request.POST,instance=customer)
        if(form.is_valid()):
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'placeOrder.html',context)
 
def addClub(request):
    form=createproductform()
    if(request.method=='POST'):
        form=createproductform(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'addClub.html',context)
 
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home') 
    else: 
        form=createuserform()
        customerform=createcustomerform()
        if request.method=='POST':
            form=createuserform(request.POST)
            customerform=createcustomerform(request.POST)
            if form.is_valid() and customerform.is_valid():
                user=form.save()
                customer=customerform.save(commit=False)
                customer.user=user 
                customer.save()
                return redirect('login')
        context={
            'form':form,
            'customerform':customerform,
        }
        return render(request,'register.html',context)
 
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       context={}
       return render(request,'login.html',context)
 
def logoutPage(request):
    logout(request)
    return redirect('/')
