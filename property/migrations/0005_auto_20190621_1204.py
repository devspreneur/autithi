# Generated by Django 2.2 on 2019-06-21 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20190621_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proparty',
            name='accommodates',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='proparty',
            name='amenities',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='proparty',
            name='cancellation_policy',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='proparty',
            name='cost_per_unit',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='proparty',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='proparty',
            name='house_rules',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='proparty',
            name='is_booked',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='proparty',
            name='number_of_badrooms',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='proparty',
            name='number_of_bathrooms',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='proparty',
            name='place_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='proparty',
            name='rental_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='proparty',
            name='times_viewed',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
