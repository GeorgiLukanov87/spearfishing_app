# Generated by Django 4.2.2 on 2023-06-29 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_alter_event_start_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='start_date',
        ),
    ]
