# Generated by Django 3.1.4 on 2020-12-21 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0018_auto_20201220_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_profile',
            name='staff_id',
            field=models.CharField(blank=True, default='ANC130449', max_length=10, null=True),
        ),
    ]
