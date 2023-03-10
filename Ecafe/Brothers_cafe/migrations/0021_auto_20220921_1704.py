# Generated by Django 3.2.4 on 2022-09-21 11:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Brothers_cafe', '0020_auto_20220921_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 21, 17, 4, 14, 249796)),
        ),
        migrations.RemoveField(
            model_name='food',
            name='dislike',
        ),
        migrations.AddField(
            model_name='food',
            name='dislike',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.RemoveField(
            model_name='food',
            name='like',
        ),
        migrations.AddField(
            model_name='food',
            name='like',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 21, 17, 4, 14, 249796)),
        ),
    ]
