from django.db import models
from django.urls import reverse


class Kategoria(models.Model):
    kategoria_name = models.CharField(max_length=60)
    kategoria_image = models.ImageField(upload_to='photos/kategorie', blank=True)
    slug = models.SlugField(max_length=60, unique=True)
    description = models.CharField(max_length=300)
    

    class Meta:
        verbose_name = 'kategoria'
        verbose_name_plural = 'kategorie'



    def __str__(self):
        return self.kategoria_name
    
    
    def get_url(self):
        return reverse('produkty_by_kategoria', args=[self.slug])

