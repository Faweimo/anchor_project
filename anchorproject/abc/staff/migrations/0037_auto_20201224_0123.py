# Generated by Django 3.1.4 on 2020-12-24 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0036_auto_20201224_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffprofile',
            name='staff_id',
            field=models.CharField(blank=True, default='ANC130799', max_length=10, null=True),
        ),
    ]
