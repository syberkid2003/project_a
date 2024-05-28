# Generated by Django 5.0.4 on 2024-04-16 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0006_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='college',
            name='postal_code',
        ),
        migrations.AlterField(
            model_name='college',
            name='university',
            field=models.CharField(choices=[('SVUTPT', 'Sri Venkataswara University , Tirupati'), ('APUVIZ', 'Andra University ,  Visakhapatnam')], max_length=6),
        ),
    ]
