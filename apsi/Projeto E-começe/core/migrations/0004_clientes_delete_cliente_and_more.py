# Generated by Django 5.1 on 2024-08-31 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_cliente_delete_clientes_and_more'),
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
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.AlterField(
            model_name='produto',
            name='valorComDesconto',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='produto',
            name='valorSemDesconto',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
