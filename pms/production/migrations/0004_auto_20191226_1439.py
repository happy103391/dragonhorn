# Generated by Django 3.0 on 2019-12-26 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0003_matirial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matirial',
            name='m_status',
            field=models.CharField(choices=[('Enough:', 'good'), ('Out of stuck:', 'remember to call')], default='Out of stuck', max_length=50),
        ),
    ]
