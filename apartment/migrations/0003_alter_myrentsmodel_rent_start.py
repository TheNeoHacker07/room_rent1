# Generated by Django 5.0.7 on 2024-07-21 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myrentsmodel',
            name='rent_start',
            field=models.DateField(),
        ),
    ]
