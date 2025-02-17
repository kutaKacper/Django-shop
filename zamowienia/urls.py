from django.urls import path
from . import views

urlpatterns = [
    path('apply_coupon/', views.apply_coupon, name='apply_coupon'),
    path('delete_coupon/', views.delete_coupon, name='delete_coupon'),
]