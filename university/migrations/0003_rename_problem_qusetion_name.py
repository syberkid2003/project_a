# Generated by Django 5.0.4 on 2024-04-16 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0002_qusetion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qusetion',
            old_name='problem',
            new_name='name',
        ),
    ]