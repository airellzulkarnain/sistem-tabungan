from django.http.request import HttpRequest
from django.http.response import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from login.models import User
from django.urls import reverse
from django.utils import timezone
from django.db import IntegrityError

# Create your views here.
def login(request):
    try:
        get_object_or_404(User, pk=request.POST["username"], password=request.POST["password"])
    except (KeyError):
        return render(request, 'login/index.html')
    except (Http404):
        return render(request, 'login/index.html', {"error_message": "User or Password invalid."})
    else:
        user = User.objects.get(pk=request.POST["username"])
        if user.online_status == 0:
            status = User.objects.get(pk=request.POST["username"])
            status.online_status = 1
            status.last_login = timezone.now()
            status.save()
            request.session['username'] = request.POST["username"]
            return HttpResponseRedirect(reverse('tabungan:home', args=(request.POST["username"],)))
        return render(request, 'login/index.html', {"error_message": "User logged in another device."})

def register(request):
    try:
        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        if password == confirm_password and password != "":
            user = User(username=username, password=password, last_login=timezone.now())
            user.save(force_insert=True)
        elif password != confirm_password:
            return render(request, 'register/index.html', {"error_message": "password did not match. "})
    except (KeyError):
        return render(request, 'register/index.html')
    except (IntegrityError):
        return render(request, 'register/index.html', {"error_message": "Username laready exists. "})
    else:
        return HttpResponseRedirect(reverse('login:login'))

def logout(request):
    user = User.objects.get(pk=request.session["username"])
    user.online_status = 0
    user.save()
    del request.session["username"]
    return HttpResponseRedirect(reverse('login:login'))
# def visitor_ip_address(request):

#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return ip