# Generated by Django 3.1.4 on 2020-12-21 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0020_auto_20201221_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_profile',
            name='staff_id',
            field=models.CharField(blank=True, default='ANC130107', max_length=10, null=True),
        ),
    ]