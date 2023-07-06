# Generated by Django 4.2.2 on 2023-07-06 16:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='description',
            field=models.TextField(max_length=1500, validators=[django.core.validators.MinLengthValidator(3, message='Story description must be at least 3 characters!')]),
        ),
        migrations.AlterField(
            model_name='story',
            name='title',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3, message='Story title must be at least 3 characters!')]),
        ),
    ]
