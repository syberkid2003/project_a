# Generated by Django 5.0.4 on 2024-05-03 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0025_delete_chash_delete_clang_delete_cpplang_delete_dbms_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=12)),
                ('test', models.IntegerField()),
                ('payment', models.CharField(max_length=50)),
                ('time', models.DateTimeField()),
                ('pay_time', models.DateTimeField()),
                ('test_time', models.DateTimeField()),
                ('test_due', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Clang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=12)),
                ('test', models.IntegerField()),
                ('payment', models.CharField(max_length=50)),
                ('time', models.DateTimeField()),
                ('pay_time', models.DateTimeField()),
                ('test_time', models.DateTimeField()),
                ('test_due', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CPPlang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=12)),
                ('test', models.IntegerField()),
                ('payment', models.CharField(max_length=50)),
                ('time', models.DateTimeField()),
                ('pay_time', models.DateTimeField()),
                ('test_time', models.DateTimeField()),
                ('test_due', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='DBMS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=12)),
                ('test', models.IntegerField()),
                ('payment', models.CharField(max_length=50)),
                ('time', models.DateTimeField()),
                ('pay_time', models.DateTimeField()),
                ('test_time', models.DateTimeField()),
                ('test_due', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='GOlang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=12)),
                ('test', models.IntegerField()),
                ('payment', models.CharField(max_length=50)),
                ('time', models.DateTimeField()),
                ('pay_time', models.DateTimeField()),
                ('test_time', models.DateTimeField()),
                ('test_due', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='HTML',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=12)),
                ('test', models.IntegerField()),
                ('payment', models.CharField(max_length=50)),
                ('time', models.DateTimeField()),
                ('pay_time', models.DateTimeField()),
                ('test_time', models.DateTimeField()),
                ('test_due', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Java',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=12)),
                ('test', models.IntegerField()),
                ('payment', models.CharField(max_length=50)),
                ('time', models.DateTimeField()),
                ('pay_time', models.DateTimeField()),
                ('test_time', models.DateTimeField()),
                ('test_due', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='JavaScript',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=12)),
                ('test', models.IntegerField()),
                ('payment', models.CharField(max_length=50)),
                ('time', models.DateTimeField()),
                ('pay_time', models.DateTimeField()),
                ('test_time', models.DateTimeField()),
                ('test_due', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PHP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=12)),
                ('test', models.IntegerField()),
                ('payment', models.CharField(max_length=50)),
                ('time', models.DateTimeField()),
                ('pay_time', models.DateTimeField()),
                ('test_time', models.DateTimeField()),
                ('test_due', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Python',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=12)),
                ('test', models.IntegerField()),
                ('payment', models.CharField(max_length=50)),
                ('time', models.DateTimeField()),
                ('pay_time', models.DateTimeField()),
                ('test_time', models.DateTimeField()),
                ('test_due', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Rlang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=12)),
                ('test', models.IntegerField()),
                ('payment', models.CharField(max_length=50)),
                ('time', models.DateTimeField()),
                ('pay_time', models.DateTimeField()),
                ('test_time', models.DateTimeField()),
                ('test_due', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='RUST',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=12)),
                ('test', models.IntegerField()),
                ('payment', models.CharField(max_length=50)),
                ('time', models.DateTimeField()),
                ('pay_time', models.DateTimeField()),
                ('test_time', models.DateTimeField()),
                ('test_due', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='SWIFT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=12)),
                ('test', models.IntegerField()),
                ('payment', models.CharField(max_length=50)),
                ('time', models.DateTimeField()),
                ('pay_time', models.DateTimeField()),
                ('test_time', models.DateTimeField()),
                ('test_due', models.DateTimeField()),
            ],
        ),
    ]
