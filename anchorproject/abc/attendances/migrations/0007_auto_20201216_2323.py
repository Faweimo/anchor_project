# Generated by Django 3.1.4 on 2020-12-16 23:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendances', '0006_auto_20201216_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='attendance_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='clock_in',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 16, 23, 23, 49, 306671)),
        ),
    ]