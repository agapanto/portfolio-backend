# Generated by Django 2.2 on 2019-04-30 06:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agapanto_portfolios', '0006_auto_20190430_0626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioitem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portfolioitems', to=settings.AUTH_USER_MODEL),
        ),
    ]
