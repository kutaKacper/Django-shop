from django.urls import path
from . import views


urlpatterns = [
    path('', views.koszyk, name='koszyk'),
    path('add_koszyk/<int:produkt_id>/', views.add_koszyk, name='add_koszyk'),
    path('delete_koszyk/<int:produkt_id>/', views.delete_koszyk, name='delete_koszyk'),
    path('delete_item/<int:produkt_id>/', views.delete_item, name='delete_item'),
    path('checkout/', views.checkout, name='checkout'),
]