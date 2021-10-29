from django.shortcuts import render

def golfshop(request):
    return render(request, 'golfshop_home.html')
