# Generated by Django 5.0.6 on 2024-06-13 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Produtos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='foto',
            field=models.ImageField(default='Sem Valor', upload_to='foto_perfil/'),
            preserve_default=False,
        ),
    ]
