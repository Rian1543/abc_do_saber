# Generated by Django 5.0.8 on 2024-08-22 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titulo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titulo',
            name='descricao',
            field=models.CharField(help_text='Informe a descricao do titulo', max_length=70),
        ),
    ]
