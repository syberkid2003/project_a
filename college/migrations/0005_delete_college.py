# Generated by Django 5.0.4 on 2024-04-16 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0004_alter_college_city_alter_college_clg_code_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='College',
        ),
    ]