# Generated by Django 3.1.2 on 2020-10-18 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20201015_2214'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyertoBids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.listings')),
            ],
        ),
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('bid_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('status', models.CharField(choices=[('Open', 'Closed'), ('Won', 'Lost')], max_length=6)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.listings')),
            ],
        ),
    ]
