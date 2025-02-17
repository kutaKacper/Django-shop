from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

from zamowienia.models import Zamowienie
from .models import Produkt
from kategoria.models import Kategoria
from koszyki.models import KoszykItem
from koszyki.views import _koszyk_id
# Create your views here.


def sklep(request, kategoria_slug=None):
    
    kategorie = None
    produkty = None

    if kategoria_slug == None:
        produkty = Produkt.objects.all().filter(is_available=True).order_by('id')
        produkt_count = produkty.filter(~Q(stock=0)).count()
        paginator = Paginator(produkty, 6)
        page = request.GET.get('page')
        paged_produkty = paginator.get_page(page)
   
    else:
        kategorie = get_object_or_404(Kategoria, slug=kategoria_slug)
        produkty = Produkt.objects.filter(kategoria=kategorie, is_available=True)
        produkt_count = produkty.filter(~Q(stock=0)).count()
        paginator = Paginator(produkty, 6)
        page = request.GET.get('page')
        paged_produkty = paginator.get_page(page)

    context = {
        'produkty': paged_produkty,
        'produkt_count': produkt_count,
    }
    
    return render(request, 'sklep/sklep.html', context)


def details(request, kategoria_slug, produkt_slug):
    single_produkt = Produkt.objects.get(kategoria__slug=kategoria_slug, slug=produkt_slug)

    
    context = {
        'single_produkt': single_produkt,
    }
    return render(request, 'sklep/details.html', context)


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            produkty = Produkt.objects.order_by('-created_date').filter(Q(produkt_name__icontains=keyword) | Q(description__icontains=keyword))
            produkt_count = produkty.count()
        else:
            produkty = Produkt.objects.order_by('-created_date')
            produkt_count = produkty.count()
    context = {
        'produkty': produkty,
        'produkt_count': produkt_count
    }
    return render(request, 'sklep/sklep.html', context)






def orders(request):
    current_user = request.user
    orders = Zamowienie.objects.filter(konto_id=current_user.pk)
    context = {
        'orders': orders,
    }
    return render(request, 'sklep/zamowienia.html', context)
