# Generated by Django 4.0.3 on 2022-08-25 01:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_step_ingredient'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Step',
        ),
    ]
