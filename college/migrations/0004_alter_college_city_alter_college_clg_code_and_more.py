# Generated by Django 5.0.4 on 2024-04-15 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='city',
            field=models.CharField(max_length=54),
        ),
        migrations.AlterField(
            model_name='college',
            name='clg_code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='college',
            name='university',
            field=models.CharField(max_length=254),
        ),
    ]
