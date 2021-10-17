from django.shortcuts import render
#from django.http import Http404
from .models import ProductID

# Create your views here.
def home(request):
    products=ProductID.objects.all()
    return render(request, "home.html", {'products':products,})

''' #defining a pet page and rendering
def pet_detail(request,pet_id):
    try:
        #perform an ORM query to get specific pet
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        #show an appropriate 404 message
        raise Http404("Pet not found")
    return render(request, 'pet_detail.html', {'pet':pet,})
    '''