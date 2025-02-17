from django.urls import path
from . import views

urlpatterns = [
    path('', views.sklep, name='sklep'),
    path('kategoria/<slug:kategoria_slug>/', views.sklep, name='produkty_by_kategoria'),
    path('kategoria/<slug:kategoria_slug>/<slug:produkt_slug>/', views.details, name='details'),
    path('search/', views.search, name='search'),
    path('zamowienia', views.orders, name='orders'),
]