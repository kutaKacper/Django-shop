# Generated by Django 4.2.9 on 2024-03-29 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zamowienia', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='zamowienie',
            old_name='konto_id',
            new_name='konto',
        ),
    ]
