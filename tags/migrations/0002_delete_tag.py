# Generated by Django 4.0.3 on 2022-08-25 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tag',
        ),
    ]