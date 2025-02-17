from django.utils import timezone
from django.db import models

from konta.models import Konto



class Zamowienie(models.Model):
    total = models.DecimalField(max_digits=8, decimal_places=2)
    address = models.CharField(max_length=250)
    konto = models.ForeignKey(Konto, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=250)
    

    class Meta:
        verbose_name = 'zamówienie'
        verbose_name_plural = 'zamówienia'


    def __str__(self):
        return "Zamowienie " + str(self.pk)
    

class Kupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    valid_from = models.DateTimeField(default=timezone.datetime(2024, 1, 1), blank=True, null=True)
    valid_to = models.DateTimeField(default=timezone.datetime(2100, 1, 1), blank=True, null=True)
    active = models.BooleanField(default=True)
    redeem_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'kupony'
        verbose_name_plural = 'kupon'

    def __str__(self):
        return self.code