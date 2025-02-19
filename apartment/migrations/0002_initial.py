# Generated by Django 5.0.7 on 2024-07-21 17:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apartment', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='apartmentmodel',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='apart_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='myrentsmodel',
            name='aparments',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apartment', to='apartment.apartmentmodel'),
        ),
        migrations.AddField(
            model_name='myrentsmodel',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
