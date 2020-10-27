# Generated by Django 3.1.2 on 2020-10-21 03:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20201020_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='watchlist',
            field=models.ManyToManyField(related_name='listing_watchlist', to=settings.AUTH_USER_MODEL),
        ),
    ]