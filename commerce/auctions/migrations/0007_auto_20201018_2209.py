# Generated by Django 3.1.2 on 2020-10-18 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_buyer_buyertobids'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyer',
            name='listing',
        ),
        migrations.DeleteModel(
            name='BuyertoBids',
        ),
        migrations.DeleteModel(
            name='Buyer',
        ),
    ]
