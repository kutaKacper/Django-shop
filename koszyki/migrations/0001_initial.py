# Generated by Django 4.2.9 on 2024-03-24 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sklep', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Koszyk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('koszyk_id', models.CharField(blank=True, max_length=250)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='KoszykItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('koszyk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='koszyki.koszyk')),
                ('produkt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sklep.produkt')),
            ],
        ),
    ]
