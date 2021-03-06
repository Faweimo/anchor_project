# Generated by Django 3.1.4 on 2020-12-14 15:08

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_id', models.CharField(blank=True, default='ANC130385', max_length=7, null=True)),
                ('email', models.CharField(max_length=100)),
                ('department', models.CharField(blank=True, max_length=100, null=True)),
                ('display_pics', models.ImageField(blank=True, default='avatar.png', null=True, upload_to='profile pics')),
                ('time', models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 14, 15, 8, 32, 455535, tzinfo=utc))),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
