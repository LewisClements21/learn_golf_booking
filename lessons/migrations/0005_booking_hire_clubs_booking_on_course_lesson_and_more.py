# Generated by Django 5.1 on 2024-09-08 22:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0004_booking_user_alter_booking_email_alter_booking_name_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='hire_clubs',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='on_course_lesson',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
