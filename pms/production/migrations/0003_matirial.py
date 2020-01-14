# Generated by Django 3.0 on 2019-12-26 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0002_auto_20191226_0338'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matirial',
            fields=[
                ('m_number', models.IntegerField(primary_key=True, serialize=False)),
                ('m_name', models.CharField(max_length=10)),
                ('m_status', models.CharField(default='缺貨', max_length=50)),
                ('m_left_amount', models.IntegerField()),
                ('m_safe_inventory', models.DecimalField(decimal_places=0, max_digits=3)),
            ],
        ),
    ]
