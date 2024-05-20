# Generated by Django 5.0.4 on 2024-04-15 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0003_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('hall_no', models.CharField(max_length=50)),
                ('college', models.CharField(max_length=254)),
                ('clg_code', models.CharField(max_length=10)),
            ],
        ),
    ]
