# Generated by Django 3.1.4 on 2020-12-14 15:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_auto_20201214_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff_profile',
            name='level',
            field=models.CharField(blank=True, default='Novice', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='staff_profile',
            name='staff_id',
            field=models.CharField(blank=True, default='ANC130775', max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='staff_profile',
            name='work_from',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 14, 15, 44, 57, 636060, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='staff_profile',
            name='work_to',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 14, 15, 44, 57, 636105, tzinfo=utc)),
        ),
    ]