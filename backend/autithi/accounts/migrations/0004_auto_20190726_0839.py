# Generated by Django 2.1.5 on 2019-07-26 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_user_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='longitude',
            field=models.BooleanField(default=True),
        ),
    ]
