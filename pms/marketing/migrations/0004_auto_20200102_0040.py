# Generated by Django 3.0 on 2020-01-01 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0003_auto_20200101_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purrecord',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketing.Customer'),
        ),
    ]
