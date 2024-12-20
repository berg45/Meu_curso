# Generated by Django 5.1 on 2024-08-29 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=150)),
                ('cpf_cnpj', models.CharField(max_length=150)),
                ('cep', models.TextField(max_length=11)),
                ('endereço', models.TextField(max_length=150)),
                ('bairro', models.TextField(max_length=150)),
                ('numero', models.TextField(max_length=5)),
                ('cidade', models.TextField(max_length=30)),
                ('estado', models.TextField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_produto', models.ImageField(upload_to='imgagem_produto/')),
                ('nome_produto', models.CharField(max_length=40)),
                ('descricao', models.TextField(max_length=200)),
                ('valorComDesconto', models.DecimalField(decimal_places=2, max_digits=4)),
                ('valorSemDesconto', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
    ]
