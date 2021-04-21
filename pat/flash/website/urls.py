from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='k'),
    path('add.html', views.add, name='add'),
    path('divide.html', views.divide, name='divide'),
    path('multiply.html', views.multiply, name='multiply'),
    path('subtract.html', views.subtract, name='subtract'),

]
