from django.db.utils import IntegrityError
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.db import DataError
from django.utils import timezone
from django.urls import reverse
from django.http import Http404
from login.models import User
from tabungan.models import Transaction

# Create your views here.
def home(request, user):
    if user != request.session["username"]: 
        raise Http404("Incorrect URL")
    user = get_object_or_404(User, pk=request.session["username"])
    return render(request, 'tabungan/home.html', {
        "user": request.session["username"], 
        "tabungan": user, 
    })

def withdrawal(request, user, nama_tabungan):
    user = get_object_or_404(User, pk=request.session["username"])
    tabungan = get_object_or_404(user.saving_set, name=nama_tabungan.replace('_', ' '))
    tabungan.delete()
    return HttpResponseRedirect(reverse('tabungan:home', args=(request.session["username"], )))


def add(request, user):
    user = get_object_or_404(User, pk=request.session["username"])
    try:
        for test_el in ["name", "target", "timespayment"]:
            request.POST[test_el]
    except (KeyError):
        return render(request, 'tabungan/add.html', {"user" : request.session["username"]})
    else:
        try:
            user.saving_set.create(
                name = request.POST["name"].lower(), 
                owned_by=user, 
                target = request.POST["target"], 
                created_date = timezone.now(), 
                jumlah_pembayaran = request.POST["timespayment"]
            )
        except (ValidationError, DataError): 
            return render(request, 'tabungan/add.html', {"error_message": "please enter the correct value", "user": request.session["username"]})
        except (IntegrityError):
            return render(request, 'tabungan/add.html', {"error_message": "saving with the same name already exist.", "user": request.session["username"]})
        else: 
            return HttpResponseRedirect(reverse('tabungan:home', args=(request.session["username"], )))

def tabungan(request, user, nama_tabungan):
    user = get_object_or_404(User, pk=request.session["username"])
    tabungan = get_object_or_404(user.saving_set, name=nama_tabungan.replace('_', ' '))
    return render(request, 'tabungan/tabungan.html', {
        'user': user.username, 
        'date': tabungan.created_date, 
        'nama_tabungan': tabungan.name, 
        'transactions': tabungan, 
        'total' : sum([transaction.amount for transaction in tabungan.transaction_set.all()])
        })

def pay(request, user, nama_tabungan):
    user = get_object_or_404(User, pk=request.session["username"])
    tabungan = get_object_or_404(user.saving_set, name=nama_tabungan.replace('_', ' '))
    if sum([transaction.amount for transaction in tabungan.transaction_set.all()]) < tabungan.target : 
        tabungan.transaction_set.create(saver_name=user, saving_name=tabungan, amount=tabungan.target/tabungan.jumlah_pembayaran, payment_date=timezone.now())
    if sum([transaction.amount for transaction in tabungan.transaction_set.all()]) >= tabungan.target : 
        tabungan.status = "sudah lunas."
        tabungan.save()
    return HttpResponseRedirect(reverse('tabungan:tabungan', args=(user.username, tabungan.name)))

def redirect(request):
    try: 
        request.session["username"]
    except: 
        return HttpResponseRedirect(reverse('login:login'))
    else: 
        return HttpResponseRedirect(reverse('tabungan:home', args=(request.session["username"],)))

