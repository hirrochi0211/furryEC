# Generated by Django 2.2 on 2021-11-10 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coursechapter',
            old_name='courses',
            new_name='course',
        ),
    ]
