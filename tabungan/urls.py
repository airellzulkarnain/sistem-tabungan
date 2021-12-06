from django.urls import path
from . import views

app_name='tabungan'

urlpatterns = [
    path('<str:user>/tabungan/', views.home, name='home'), 
    path('<str:user>/tabungan/add/', views.add, name='add'), 
    path('', views.redirect),
    
]