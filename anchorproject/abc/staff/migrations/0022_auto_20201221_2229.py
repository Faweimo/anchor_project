# Generated by Django 3.1.4 on 2020-12-21 22:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('staff', '0021_auto_20201221_0203'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffProfiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_id', models.CharField(blank=True, default='ANC130410', max_length=10, null=True)),
                ('department', models.CharField(default='worker', max_length=100)),
                ('display_pics', models.ImageField(blank=True, default='avatar.png', null=True, upload_to='profile pics')),
                ('level', models.CharField(blank=True, default='Novice', max_length=100, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Staff_profile',
        ),
    ]
