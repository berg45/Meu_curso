# Generated by Django 5.1.2 on 2024-10-18 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='curtidas',
        ),
        migrations.AddField(
            model_name='post',
            name='imagem',
            field=models.ImageField(default='1', upload_to='imagens/'),
            preserve_default=False,
        ),
    ]
