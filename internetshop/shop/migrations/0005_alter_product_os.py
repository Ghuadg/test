# Generated by Django 5.0.6 on 2024-07-05 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_os_product_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='os',
            field=models.TextField(blank=True, null=True),
        ),
    ]
