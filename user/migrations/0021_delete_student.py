# Generated by Django 5.0.4 on 2024-05-03 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_alter_student_user_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
    ]
