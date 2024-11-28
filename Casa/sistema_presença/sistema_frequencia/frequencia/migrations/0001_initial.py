# Generated by Django 5.1 on 2024-11-12 18:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('ano', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Presenca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('presente', models.BooleanField(default=False)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frequencia.aluno')),
            ],
        ),
        migrations.AddField(
            model_name='aluno',
            name='turma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alunos', to='frequencia.turma'),
        ),
    ]
