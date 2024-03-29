# Generated by Django 4.2.1 on 2023-10-18 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_user1_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeeklyAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_start', models.DateField()),
                ('sunday_available', models.BooleanField(default=False)),
                ('sunday_start_time', models.TimeField(blank=True, null=True)),
                ('sunday_end_time', models.TimeField(blank=True, null=True)),
                ('monday_available', models.BooleanField(default=False)),
                ('monday_start_time', models.TimeField(blank=True, null=True)),
                ('monday_end_time', models.TimeField(blank=True, null=True)),
                ('tuesday_available', models.BooleanField(default=False)),
                ('tuesday_start_time', models.TimeField(blank=True, null=True)),
                ('tuesday_end_time', models.TimeField(blank=True, null=True)),
                ('wednesday_available', models.BooleanField(default=False)),
                ('wednesday_start_time', models.TimeField(blank=True, null=True)),
                ('wednesday_end_time', models.TimeField(blank=True, null=True)),
                ('thursday_available', models.BooleanField(default=False)),
                ('thursday_start_time', models.TimeField(blank=True, null=True)),
                ('thursday_end_time', models.TimeField(blank=True, null=True)),
                ('friday_available', models.BooleanField(default=False)),
                ('friday_start_time', models.TimeField(blank=True, null=True)),
                ('friday_end_time', models.TimeField(blank=True, null=True)),
                ('saturday_available', models.BooleanField(default=False)),
                ('saturday_start_time', models.TimeField(blank=True, null=True)),
                ('saturday_end_time', models.TimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user1')),
            ],
        ),
    ]
