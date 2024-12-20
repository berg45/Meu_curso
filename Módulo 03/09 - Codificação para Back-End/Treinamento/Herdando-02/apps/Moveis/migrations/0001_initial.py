# Generated by Django 5.0.6 on 2024-06-26 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('cpf', models.PositiveBigIntegerField()),
                ('crear_senha', models.CharField(max_length=15)),
                ('confirmar_senha', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('categoria', models.CharField(max_length=20)),
                ('imagem', models.ImageField(upload_to='imagem/')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
