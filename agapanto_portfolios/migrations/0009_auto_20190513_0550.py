# Generated by Django 2.2 on 2019-05-13 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agapanto_portfolios', '0008_auto_20190513_0537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]