# Generated by Django 4.1.6 on 2023-02-16 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='holidays',
            old_name='Price',
            new_name='Price_USD',
        ),
    ]
