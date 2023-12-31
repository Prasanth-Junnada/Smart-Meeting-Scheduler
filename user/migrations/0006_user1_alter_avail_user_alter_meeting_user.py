# Generated by Django 4.1.7 on 2023-08-17 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_user_otp_user_verify'),
    ]

    operations = [
        migrations.CreateModel(
            name='User1',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('fullname', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('otp', models.IntegerField(null=True)),
                ('verify', models.CharField(default='no', max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='avail',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user1'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user1'),
        ),
    ]
