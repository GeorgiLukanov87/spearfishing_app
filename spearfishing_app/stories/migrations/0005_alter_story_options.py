# Generated by Django 4.2.2 on 2023-07-25 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0004_alter_story_creator'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='story',
            options={'verbose_name_plural': 'Stories'},
        ),
    ]
