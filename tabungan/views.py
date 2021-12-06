from django.db.utils import IntegrityError
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.db import DataError
from django.utils import timezone
from django.urls import reverse
from login.models import User

# Create your views here.
def home(request, user):
    user = get_object_or_404(User, pk=request.session["username"])
    return render(request, 'tabungan/home.html', {
        "user": request.session["username"], 
        "tabungan": user, 
    })

def add(request, user):
    user = get_object_or_404(User, pk=request.session["username"])
    try:
        for test_el in ["name", "target", "noticeevery", "timespayment"]:
            request.POST[test_el]
    except (KeyError):
        return render(request, 'tabungan/add.html', {"user" : request.session["username"] })
    else:
        try:
            user.saving_set.create(
                name = request.POST["name"].lower(), 
                owned_by=user, 
                target = request.POST["target"], 
                created_date = timezone.now(), 
                notice_every = request.POST["noticeevery"], 
                jumlah_pembayaran = request.POST["timespayment"]
            )
        except (ValidationError, DataError): 
            return render(request, 'tabungan/add.html', {"error_message": "please enter the correct value", "user": request.session["username"]})
        except (IntegrityError):
            return render(request, 'tabungan/add.html', {"error_message": "saving with the same name already exist.", "user": request.session["username"]})
        else: 
            return HttpResponseRedirect(reverse('tabungan:home', args=(request.session["username"], )))

def redirect(request):
    return HttpResponseRedirect(reverse('login:login'))