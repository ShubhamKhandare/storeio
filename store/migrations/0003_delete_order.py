# Generated by Django 3.1.7 on 2021-03-22 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]
