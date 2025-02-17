from .models import Koszyk, KoszykItem
from .views import _koszyk_id


def counter(request):
    w_koszyku = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            koszyk = Koszyk.objects.filter(koszyk_id=_koszyk_id(request))
            koszyk_items = KoszykItem.objects.all().filter(koszyk=koszyk[:1])
            for item in koszyk_items:
                w_koszyku += item.amount
        except Koszyk.DoesNotExist:
            w_koszyku = 0
    return dict(w_koszyku=w_koszyku)