# Generated by Django 2.1.5 on 2019-06-28 13:16

import autithi.utils.location
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recommendation', '0001_initial'),
        ('city', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proparty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.SlugField()),
                ('description', models.TextField(blank=True, null=True)),
                ('cost_per_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('place_type', models.CharField(blank=True, max_length=255, null=True)),
                ('rental_type', models.CharField(blank=True, max_length=255, null=True)),
                ('house_rules', models.TextField(blank=True, null=True)),
                ('cancellation_policy', models.TextField(blank=True, null=True)),
                ('amenities', models.CharField(blank=True, max_length=255, null=True)),
                ('number_of_badrooms', models.IntegerField(blank=True, null=True)),
                ('number_of_bathrooms', models.IntegerField(blank=True, null=True)),
                ('number_of_guest', models.IntegerField(blank=True, null=True)),
                ('accommodates', models.CharField(blank=True, max_length=255, null=True)),
                ('times_viewed', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('address', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='propartys', to='accounts.Address')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='propartys', to='city.City')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='propartys', to=settings.AUTH_USER_MODEL)),
                ('recommendation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='propartys', to='recommendation.Recommendation')),
            ],
        ),
        migrations.CreateModel(
            name='PropartyImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=autithi.utils.location.upload_location)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('proparty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proparty.Proparty')),
            ],
        ),
    ]