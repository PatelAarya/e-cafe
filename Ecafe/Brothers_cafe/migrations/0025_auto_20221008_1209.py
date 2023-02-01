# Generated by Django 3.2.4 on 2022-10-08 06:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Brothers_cafe', '0024_auto_20221008_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='food_name',
        ),
        migrations.AddField(
            model_name='cart',
            name='food_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Brothers_cafe.food'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 8, 12, 9, 47, 153428)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 8, 12, 9, 47, 153428)),
        ),
    ]
