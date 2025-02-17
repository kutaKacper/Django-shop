# Generated by Django 4.2.9 on 2024-03-24 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('kategoria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produkt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produkt_name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('short_description', models.TextField(blank=True, max_length=2000)),
                ('description', models.TextField(blank=True, max_length=5000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('stock', models.IntegerField()),
                ('is_available', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('kategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kategoria.kategoria')),
                ('photo', models.ImageField(upload_to='photos/produkty')),
            ],
        ),
    ]
