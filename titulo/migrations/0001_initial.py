# Generated by Django 5.0.8 on 2024-08-22 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Titulo',
            fields=[
                ('codigo', models.AutoField(help_text='Codigo do titulo', primary_key=True, serialize=False)),
                ('descricao', models.CharField(help_text='Informe a descricao do tipo de atividade', max_length=70)),
            ],
        ),
    ]
