# Generated by Django 5.0.4 on 2024-05-11 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerSupport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('_from', models.CharField(max_length=50)),
                ('emp_id', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('solution', models.TextField()),
            ],
        ),
    ]
