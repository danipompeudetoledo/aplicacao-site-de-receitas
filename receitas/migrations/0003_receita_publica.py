# Generated by Django 4.0.1 on 2022-02-03 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0002_receita_pessoa'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='publica',
            field=models.BooleanField(default=False),
        ),
    ]
