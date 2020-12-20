# Generated by Django 3.1.4 on 2020-12-14 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0006_auto_20201214_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff_profile',
            name='team_leader',
        ),
        migrations.RemoveField(
            model_name='staff_profile',
            name='work_from',
        ),
        migrations.RemoveField(
            model_name='staff_profile',
            name='work_title',
        ),
        migrations.RemoveField(
            model_name='staff_profile',
            name='work_to',
        ),
        migrations.AlterField(
            model_name='staff_profile',
            name='department',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='staff_profile',
            name='staff_id',
            field=models.CharField(blank=True, default='ANC130457', max_length=10, null=True),
        ),
    ]