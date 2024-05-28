# Generated by Django 5.0.4 on 2024-04-15 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('college', '0002_delete_college'),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('university', models.EmailField(max_length=254)),
                ('clg_code', models.EmailField(max_length=10)),
                ('city', models.EmailField(max_length=54)),
            ],
        ),
    ]