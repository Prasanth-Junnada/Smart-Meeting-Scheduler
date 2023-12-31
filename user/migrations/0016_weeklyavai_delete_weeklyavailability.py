# Generated by Django 4.2.1 on 2023-10-18 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_alter_weeklyavailability_week_start'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeeklyAvai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('sun', 'Sunday'), ('mon', 'Monday'), ('tue', 'Tuesday'), ('wed', 'Wednesday'), ('thr', 'Thursday'), ('fri', 'Friday'), ('sat', 'Saturday')], max_length=3)),
                ('available', models.BooleanField(default=False)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user1')),
            ],
        ),
        migrations.DeleteModel(
            name='WeeklyAvailability',
        ),
    ]
