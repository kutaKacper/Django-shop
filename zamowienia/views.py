import sys
from django.shortcuts import redirect, render
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

from zamowienia.utils import calculate_discount
from .models import Kupon


def apply_coupon(request):
    if request.method == 'POST':
        coupon_code = request.POST.get('coupon_code')
        try:
            coupon = Kupon.objects.get(code=coupon_code, 
                                         valid_from__lte=timezone.now(),
                                         valid_to__gte=timezone.now(),
                                         active=True)
            coupon.active = False
            coupon.redeem_date = timezone.now()
            coupon.save()
            total = request.session.get('total', 0)
            total_cost = calculate_discount(total, coupon.percentage)
            request.session['total_discounted'] = total_cost
            request.session['discount_percentage'] = float(coupon.percentage)
            request.session['coupon_code'] = coupon_code
            return redirect('koszyk')
        except (Kupon.DoesNotExist, ObjectDoesNotExist):
            return redirect('koszyk')
        

def delete_coupon(request):
    
    if request.method == 'POST':
        try:
            coupon_code = request.session.get('coupon_code')
            coupon = Kupon.objects.get(code=coupon_code)
            del request.session['total_discounted']
            del request.session['discount_percentage']
            del request.session['coupon_code']
            del request.session['discount_amount']
            
            coupon.active = True
            coupon.redeem_date = None
            coupon.save()
            return redirect('koszyk')
        except (Kupon.DoesNotExist, ObjectDoesNotExist):
            return redirect('koszyk')