# Generated by Django 5.0.6 on 2025-01-02 11:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_client_user_client_firstname_client_lastname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
