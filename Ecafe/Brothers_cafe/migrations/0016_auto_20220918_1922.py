# Generated by Django 3.2.4 on 2022-09-18 13:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Brothers_cafe', '0015_auto_20220918_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLogInDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='contact_form',
            name='lname',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 18, 19, 22, 44, 44867)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 18, 19, 22, 44, 44867)),
        ),
    ]
