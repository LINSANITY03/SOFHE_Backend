# Generated by Django 4.1.1 on 2022-10-02 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_event_task_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='credit',
            field=models.DecimalField(decimal_places=4, max_digits=14),
        ),
    ]