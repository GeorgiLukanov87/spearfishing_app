# Generated by Django 4.2.2 on 2023-06-29 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_remove_event_creator_event_creator'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='creator',
            new_name='competitors',
        ),
    ]
