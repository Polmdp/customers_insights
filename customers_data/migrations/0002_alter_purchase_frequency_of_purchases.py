# Generated by Django 5.0 on 2023-12-21 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='frequency_of_purchases',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
