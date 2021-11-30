from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from login.models import User

# Create your views here.
def home(request, user):
    get_object_or_404(User, pk=request.session["username"])
    return render(request, 'tabungan/home.html', {"user": request.session["username"]})

def redirect(request):
    return HttpResponseRedirect(reverse('login:login'))