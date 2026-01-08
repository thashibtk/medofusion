from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('products/', views.shop, name='products'),
    path('products/<slug:slug>/', views.product_details, name='product-details'),
    path('contact/', views.contact, name='contact'),
]
