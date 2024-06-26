# Generated by Django 5.0.4 on 2024-05-20 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('college', '0030_delete_chash_delete_clang_delete_college_and_more'),
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
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('university', models.CharField(choices=[('SVUTPT', 'Sri Venkataswara University , Tirupati'), ('APUVIZ', 'Andra University ,  Visakhapatnam')], max_length=6)),
                ('clg_code', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=54)),
                ('postal', models.CharField(max_length=254)),
                ('profile', models.ImageField(upload_to='profile/college/')),
                ('terms', models.CharField(max_length=6)),
                ('principal', models.CharField(max_length=60)),
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
