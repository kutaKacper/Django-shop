from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class KontoManager(BaseUserManager):
    def create_user(self, first_name, last_name, phone, email, username, password=None):
        if username == "":
            raise ValueError('Podaj nazwę użytkownika')
        if email == "":
            raise ValueError('Podaj adres e-mail.')
        
        user = self.model(
            first_name = first_name,
            last_name = last_name,
            phone = phone,
            username = username,
            email = self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, first_name, last_name, phone, username, email, password):
        user = self.create_user(
            first_name = first_name,
            last_name = last_name,
            phone = phone,
            username = username,
            email = self.normalize_email(email),
            password = password
        )
        user.is_admin = True
        user.is_superadmin = True
        user.is_staff = True
        user.is_active = True

        user.save(using=self._db)
        return user
    


class Konto(AbstractBaseUser):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=40, unique=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'email']
    USERNAME_FIELD = 'username'

    objects = KontoManager()

    class Meta:
        verbose_name = 'konto'
        verbose_name_plural = 'konta'

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True