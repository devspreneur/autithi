# Generated by Django 2.1.5 on 2019-02-25 08:14

from django.db import migrations, models
import property.models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propartyimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=property.models.upload_location),
        ),
    ]
