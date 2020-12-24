# Generated by Django 3.1.3 on 2020-12-24 22:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('agapanto_portfolios', '0013_auto_20201220_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='portfolioitem',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
