# Generated by Django 5.0.7 on 2024-07-11 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BergPizza', '0005_pedido_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='cliente',
        ),
    ]
