# Generated by Django 4.1.5 on 2023-05-19 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Attendance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancedetails',
            name='time_frame',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
