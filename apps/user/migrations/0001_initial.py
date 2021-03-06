# Generated by Django 2.1.7 on 2019-03-16 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shopping', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit_card', models.TextField(blank=True, null=True)),
                ('address_1', models.CharField(blank=True, max_length=100, null=True)),
                ('address_2', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('region', models.CharField(blank=True, max_length=100, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('day_phone', models.CharField(blank=True, max_length=100, null=True)),
                ('eve_phone', models.CharField(blank=True, max_length=100, null=True)),
                ('mob_phone', models.CharField(blank=True, max_length=100, null=True)),
                ('shipping_region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='shopping.ShippingRegion')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
    ]
