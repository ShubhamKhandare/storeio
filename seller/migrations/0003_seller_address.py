# Generated by Django 3.1.7 on 2021-03-22 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_remove_seller_seller_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='address',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]