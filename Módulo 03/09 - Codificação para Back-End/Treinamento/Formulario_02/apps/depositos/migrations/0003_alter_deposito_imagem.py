# Generated by Django 5.0.6 on 2024-07-04 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depositos', '0002_deposito_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposito',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
