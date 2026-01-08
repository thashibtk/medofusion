from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Count

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def shop(request):
    products = Product.objects.filter(is_active=True)
    categories = Category.objects.annotate(product_count=Count('products'))
    
    category_slug = request.GET.get('category')
    if category_slug:
        products = products.filter(category__slug=category_slug)
        
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'shop.html', context)

def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    
    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'product_details.html', context)

def contact(request):
    return render(request, 'contact.html')

