# Generated by Django 5.1.7 on 2025-03-09 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_api_app', '0002_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=100.0, verbose_name='Цена'),
            preserve_default=False,
        ),
    ]
