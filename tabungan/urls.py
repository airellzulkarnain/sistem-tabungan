from django.urls import path
from . import views

app_name="tabungan"

urlpatterns = [
    path('', views.home, name='home'), 
    
]