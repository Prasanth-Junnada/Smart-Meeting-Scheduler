# Generated by Django 4.1.7 on 2023-08-17 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_meeting_mail'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='day',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='meeting',
            name='time',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
