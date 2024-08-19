# Generated by Django 5.0.6 on 2024-07-04 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hamburguer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('quantidade', models.IntegerField()),
                ('descricao', models.TextField()),
                ('pedido', models.CharField(choices=[('NL', 'No local'), ('D', 'Delivere')], max_length=2)),
            ],
        ),
    ]
