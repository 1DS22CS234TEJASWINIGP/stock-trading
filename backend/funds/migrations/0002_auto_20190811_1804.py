# Generated by Django 2.2.4 on 2019-08-11 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funds',
            name='amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='funds',
            name='totalFund',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
