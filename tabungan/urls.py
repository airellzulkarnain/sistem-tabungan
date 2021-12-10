from django.urls import path
from . import views

app_name='tabungan'

urlpatterns = [
    path('<str:user>/tabungan/', views.home, name='home'), 
    path('<str:user>/tabungan/add/', views.add, name='add'), 
    path('<str:user>/tabungan/<str:nama_tabungan>', views.tabungan, name='tabungan'), 
    path('<str:user>/tabungan/<str:nama_tabungan>/pay', views.pay, name='pay'), 
    path('', views.redirect),
    
]