from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('post',views.post_func, name='post'),
    path('post_view/<int:id>',views.post_view, name='post_view'),
]
