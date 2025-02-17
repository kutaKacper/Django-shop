from decimal import Decimal
import sys
from django.shortcuts import render, redirect, get_object_or_404
from linie_zamowien.models import LiniaZamowienia
from sklep.models import Produkt
from zamowienia.models import Zamowienie
from zamowienia.utils import calculate_discount
from .models import Koszyk, KoszykItem
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .utils import calculate_total_price
# Create your views here.



def _koszyk_id(request):
    koszyk = request.session.session_key
    if not koszyk:
        koszyk = request.session.create()
    return koszyk
    


def add_koszyk(request, produkt_id):
    produkt = Produkt.objects.get(id=produkt_id)
    if produkt.stock == 0:
        return redirect('sklep')
    try:
        koszyk = Koszyk.objects.get(koszyk_id=_koszyk_id(request))
    except Koszyk.DoesNotExist:
        koszyk=Koszyk.objects.create(
            koszyk_id = _koszyk_id(request)
        )
    koszyk.save()

    try:
        item = KoszykItem.objects.get(produkt=produkt, koszyk=koszyk)
        item.amount += 1
        item.save()
    except KoszykItem.DoesNotExist:
        item = KoszykItem.objects.create(
            produkt = produkt,
            amount = 1,
            koszyk = koszyk
        )
        item.save()

    return redirect('koszyk')



def delete_koszyk(request, produkt_id):
    koszyk = Koszyk.objects.get(koszyk_id=_koszyk_id(request))
    produkt = get_object_or_404(Produkt, id=produkt_id)
    item = KoszykItem.objects.get(produkt=produkt, koszyk=koszyk)
    if item.amount > 1:
        item.amount -= 1
        item.save()
    else:
        item.delete()
    return redirect('koszyk')


def delete_item(request, produkt_id):
    koszyk = Koszyk.objects.get(koszyk_id=_koszyk_id(request))
    produkt = get_object_or_404(Produkt, id=produkt_id)
    item = KoszykItem.objects.get(produkt=produkt, koszyk=koszyk)
    item.delete()
    return redirect('koszyk')


def koszyk(request, total=0, amount=0, koszyk_items=None, total_discounted=0):
    try:
        koszyk = Koszyk.objects.get(koszyk_id=_koszyk_id(request))
        koszyk_items = KoszykItem.objects.filter(koszyk=koszyk, is_active=True)
        for item in koszyk_items:
            total += (item.produkt.price * item.amount)
            amount += item.amount
        total = calculate_total_price(koszyk_items)
        request.session['total'] = float(total)
        
        if 'total_discounted' in request.session:
            discount_percentage = request.session.get('discount_percentage')
            total_discounted = calculate_discount(float(total), float(discount_percentage))
            discount_amount = float(total) - total_discounted
            request.session['discount_amount'] = discount_amount
            request.session['total_discounted'] = total_discounted
        else:
            total_discounted = total
        
        #request.session['total_discounted'] = float(total_discounted)
        if total == 0:
            total = calculate_total_price(koszyk_items)
    except ObjectDoesNotExist:
        pass

    

    context = {
        'total' : total,
        'total_discounted': total_discounted,
        "amount": amount,
        'koszyk_items': koszyk_items
    }
    return render(request, 'sklep/koszyk.html', context)



def checkout(request):
    koszyk = Koszyk.objects.filter(koszyk_id=_koszyk_id(request))
    koszyk_items = KoszykItem.objects.all().filter(koszyk=koszyk[:1])
    #koszyk_items = KoszykItem.objects.filter(koszyk__koszyk_id=request.session.get('koszyk_id'))
    if 'total_discounted' in request.session:
        total_cost = Decimal(request.session.get('total_discounted'))
    else: 
        total_cost = Decimal(request.session.get('total'))
    
    order = Zamowienie.objects.create(
        total=total_cost,
        konto=request.user,
        status='Opłacone'
    )  
    
    for item in koszyk_items:
        LiniaZamowienia.objects.create(
            zamowienie=order,
            produkt=item.produkt,
            quantity=item.amount,
            price=item.produkt.price
        )
    
    koszyk_items.delete()
    
    return redirect('koszyk')