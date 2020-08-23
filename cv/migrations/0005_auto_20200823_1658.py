# Generated by Django 2.2.12 on 2020-08-23 15:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0004_auto_20200823_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
