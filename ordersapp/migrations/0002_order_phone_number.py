# Generated by Django 3.2.9 on 2021-11-27 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordersapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone_number',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
    ]
