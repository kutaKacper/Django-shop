from django.db import models
from sklep.models import Produkt


class Koszyk(models.Model):
    koszyk_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'koszyk'
        verbose_name_plural = 'koszyki'

    def __str__(self):
        return self.koszyk_id


class KoszykItem(models.Model):
    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE)
    koszyk = models.ForeignKey(Koszyk, on_delete=models.CASCADE)
    amount = models.IntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'produkt w koszyku'
        verbose_name_plural = 'produkty w koszyku'

    def sub_total(self):
        return self.produkt.price * self.amount

    def __str__(self):
        return self.produkt.produkt_name