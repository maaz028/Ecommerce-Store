from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('fetch_data',views.fetch_data, name='fetch_data'),
 
    path('store',views.store, name='store'),
    path('contact_us',views.contact_us, name='contact_us'),
    path('products/<int:pid>',views.products, name='products'),
    path('checkout',views.checkout, name='checkout'),
    path('order_func',views.order_func, name='order'),
    path('tracker',views.tracker, name='tracker'),
    path('search_results',views.search_results, name='search_results'),
]
