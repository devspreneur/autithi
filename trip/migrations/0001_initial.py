# Generated by Django 2.1.5 on 2019-02-25 11:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin_date', models.DateField()),
                ('end_date', models.DateField()),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=15)),
                ('confirmed', models.BooleanField(default=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
                ('proparty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proparty', to='property.Proparty')),
            ],
        ),
    ]
