# Generated by Django 3.0 on 2019-12-31 12:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0012_addmaterial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addmaterial',
            name='add_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
