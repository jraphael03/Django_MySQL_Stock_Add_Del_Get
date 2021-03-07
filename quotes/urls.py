from django.urls import path
from . import views;        # the period stand for this directory

urlpatterns = [
    path('', views.home, name="home" ),      #we are leaving the url space blank for the homepage but if you want you could write specific a url name
    path('about', views.about, name="about" ),
    path('add_stock', views.add_stock, name='add_stock'),
    path('delete/<stock_id>', views.delete, name="delete"), # Path passes in the id
    path('delete_stock', views.delete_stock, name='delete_stock'),
]