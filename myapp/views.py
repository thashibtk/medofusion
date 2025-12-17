from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def shop(request):
    return render(request, 'shop.html')

def product_details(request):
    return render(request, 'product_details.html')

def contact(request):
    return render(request, 'contact.html')

