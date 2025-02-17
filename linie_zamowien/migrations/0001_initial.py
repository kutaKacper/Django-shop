# Generated by Django 4.2.9 on 2024-03-29 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('zamowienia', '0001_initial'),
        ('sklep', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiniaZamowienia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('produkt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sklep.produkt')),
                ('zamowienie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zamowienia.zamowienie')),
            ],
        ),
    ]
