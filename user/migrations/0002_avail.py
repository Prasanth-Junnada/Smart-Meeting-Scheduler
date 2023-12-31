# Generated by Django 4.2.4 on 2023-08-05 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='avail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mon', models.CharField(max_length=500)),
                ('tue', models.CharField(max_length=500)),
                ('wed', models.CharField(max_length=500)),
                ('thr', models.CharField(max_length=500)),
                ('fri', models.CharField(max_length=500)),
                ('sat', models.CharField(max_length=500)),
                ('sun', models.CharField(max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
