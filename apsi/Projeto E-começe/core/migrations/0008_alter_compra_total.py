# Generated by Django 5.1 on 2024-09-10 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_compra_itemcompra_compra_produtos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
