# Generated by Django 5.0.4 on 2024-04-25 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='field_name',
            new_name='profile',
        ),
    ]