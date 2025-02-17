import sys
from django.shortcuts import redirect, render
from konta.forms import UserLoginForm, UserRegisterForm
from konta.models import Konto
from linie_zamowien.models import LiniaZamowienia
from sklep.models import Produkt
from konta.forms import UserLoginForm
from django.contrib.auth import authenticate, login as django_login
from django.contrib import messages

from zamowienia.models import Zamowienie

def home(request):
    produkty = Produkt.objects.all().filter(is_available=True)
    
    context = {
        'produkty': produkty
    }
    
    return render(request, 'home.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    context = {

    }
    return render(request, 'login.html', context)

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    context = {

    }
    return render(request, 'register.html', context)


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'], password=data['password']
            )
            
            if user is not None:
                django_login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Niepoprawny adres e-mail lub hasło.')
    context = {
        
    }
    return render(request, 'login.html', context)

def user_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if data['password'] != data['repeated_password']:
                 messages.error(request, 'Podane hasła nie są takie same.')
                 return render(request, 'register.html', {'form': form})
            user = Konto.objects.create_user(first_name=data['first_name'], last_name=data['last_name'], phone=data['phone'], username=data['email'], email=data['email'], password=data['password'])
            if user is not None:
                return redirect('/')
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
    }
    return render(request, 'register.html', context)


def moje_konto(request):
    current_user = request.user
    orders = Zamowienie.objects.filter(konto=current_user)

    orders_with_items = []
    for order in orders:
        order_items = LiniaZamowienia.objects.filter(zamowienie=order)
        produkt_names_items = []
        for item in order_items:
            produkt_name = item.produkt.produkt_name
            photo = item.produkt.photo.url
            produkt_names_items.append({'item': item, 'produkt_name': produkt_name, 'photo': photo})
        orders_with_items.append({'order': order, 'items': produkt_names_items})

    context = {
        'orders_with_items': orders_with_items
    }
    return render(request, 'mojekonto.html', context)