from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('shop/', views.shop, name='shop'),
    path('product_details/', views.product_details, name='product_details'),
    path('contact/', views.contact, name='contact'),
]
