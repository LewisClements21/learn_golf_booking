# Generated by Django 5.1 on 2024-08-13 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='booking',
            name='customer_name',
            field=models.CharField(max_length=50),
        ),
    ]
