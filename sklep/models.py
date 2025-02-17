from django.db import models
from kategoria.models import Kategoria
from django.urls import reverse


class Produkt(models.Model):
    produkt_name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=5000, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(blank=True, null=True)
    is_available = models.BooleanField(default=True)
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photos/produkty')

    class Meta:
        verbose_name = 'produkt'
        verbose_name_plural = 'produkty'

    def save(self, *args, **kwargs):
        if self.stock == '':
            self.stock = None
        super().save(*args, **kwargs)
        
    def get_url(self):
        return reverse('details', args=[self.kategoria.slug, self.slug])

    def __str__(self):
        return self.produkt_name