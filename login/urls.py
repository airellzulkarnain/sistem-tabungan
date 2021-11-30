from django.urls import path
from . import views

app_name = 'login'
urlpatterns = [
    path('', views.login, name='login'), 
    path('register/', views.register, name='registration'), 
    path('logout/',views.logout, name="logout"),
]