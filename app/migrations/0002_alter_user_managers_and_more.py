# Generated by Django 5.2.3 on 2025-06-12 16:09

import app.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', app.models.CustomUserManager()),
            ],
        ),
        migrations.RenameField(
            model_name='newsletter',
            old_name='created_at',
            new_name='subscribe_at',
        ),
    ]
