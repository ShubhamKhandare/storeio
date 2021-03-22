# Generated by Django 3.1.7 on 2021-03-22 18:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('type', models.TextField(max_length=90, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['type'],
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('store_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('store_name', models.TextField(max_length=90, unique=True)),
                ('store_address', models.TextField(max_length=255)),
                ('store_link', models.TextField(max_length=255)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stores', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['store_id'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('product_name', models.TextField(max_length=90)),
                ('product_description', models.TextField(max_length=255)),
                ('product_mrp', models.IntegerField()),
                ('product_sale_price', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product_image', models.ImageField(default='default.jpg', upload_to='')),
                ('product_category', models.ForeignKey(default='misc', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='products', to='store.category')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.store')),
            ],
            options={
                'ordering': ['product_name'],
                'unique_together': {('store', 'product_name')},
            },
        ),
    ]
