# Generated by Django 5.0.4 on 2024-04-30 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='user_name',
            field=models.CharField(max_length=60),
        ),
    ]
