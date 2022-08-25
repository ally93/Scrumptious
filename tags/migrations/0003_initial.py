# Generated by Django 4.0.3 on 2022-08-25 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipes', '0006_step'),
        ('tags', '0002_delete_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('recipes', models.ManyToManyField(related_name='tags', to='recipes.recipe')),
            ],
        ),
    ]