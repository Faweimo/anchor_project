# Generated by Django 3.1.4 on 2020-12-23 19:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worklogs', '0002_log_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_id', models.IntegerField()),
                ('full_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('department', models.CharField(blank=True, max_length=200, null=True)),
                ('team_leader', models.CharField(max_length=200)),
                ('work_title', models.CharField(max_length=200)),
                ('clock_in', models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 23, 19, 48, 59, 493572), null=True)),
                ('user_id', models.IntegerField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Log',
        ),
    ]