from .models import Kategoria
from django.db.models import Count

def menu_links(request):
    links = Kategoria.objects.all()
    annotated_links = links.annotate(produkt_count=Count('produkt'))
    context = {
            'links': links,
            'annotated_links': annotated_links,
        }

    return context