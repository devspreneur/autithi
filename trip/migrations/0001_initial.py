# Generated by Django 2.1.5 on 2019-02-06 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guest', to='property.Proparty')),
                ('proparty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proparty', to='property.Proparty')),
            ],
        ),
    ]
