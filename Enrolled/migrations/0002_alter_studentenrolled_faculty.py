# Generated by Django 4.1.5 on 2023-04-20 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
        ('Enrolled', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentenrolled',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facultyprovides', to='Account.faculty'),
        ),
    ]
