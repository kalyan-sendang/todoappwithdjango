# Generated by Django 4.0.4 on 2022-04-21 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='tasks',
            new_name='Task',
        ),
    ]
