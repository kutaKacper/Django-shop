from django.db import models

from sklep.models import Produkt
from zamowienia.models import Zamowienie


class LiniaZamowienia(models.Model):
    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    zamowienie = models.ForeignKey(Zamowienie, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'linia zamówienia'
        verbose_name_plural = 'linie zamówień'