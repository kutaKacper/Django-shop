"""
URL configuration for cmpshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('user_login', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),
    path('user_register', views.user_register, name='user_register'),
    path('sklep/', include('sklep.urls')),
    path('koszyk/', include('koszyki.urls')),
    path('zamowienia/', include('zamowienia.urls')),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('moje_konto/', views.moje_konto, name='moje_konto'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
