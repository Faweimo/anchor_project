# Generated by Django 3.1.4 on 2020-12-23 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_id', models.IntegerField()),
                ('full_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('team_leader', models.CharField(max_length=200)),
                ('work_title', models.CharField(max_length=200)),
                ('clock_in', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.IntegerField(blank=True)),
            ],
        ),
    ]
