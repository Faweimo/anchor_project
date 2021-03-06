# Generated by Django 3.1.4 on 2020-12-20 16:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('staff', '0017_auto_20201216_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_profile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='staff_profile',
            name='staff_id',
            field=models.CharField(blank=True, default='ANC130139', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='staff_profile',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
