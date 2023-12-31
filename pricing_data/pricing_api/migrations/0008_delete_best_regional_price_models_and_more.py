# Generated by Django 4.1.7 on 2023-06-01 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricing_api', '0007_best_regional_price_models_pricing_meter_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Best_regional_price_models',
        ),
        migrations.RenameField(
            model_name='pricing',
            old_name='vmsize',
            new_name='VmSku',
        ),
        migrations.RemoveField(
            model_name='pricing',
            name='availabilityId',
        ),
        migrations.AddField(
            model_name='pricing',
            name='best_price',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='pricing',
            name='best_price_region',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='pricing',
            name='pricePerDay',
            field=models.FloatField(blank=True, default='1'),
        ),
        migrations.AddField(
            model_name='pricing',
            name='pricePerMonth',
            field=models.FloatField(blank=True, default='1'),
        ),
        migrations.AddField(
            model_name='pricing',
            name='pricePerYear',
            field=models.FloatField(blank=True, default='1'),
        ),
    ]
