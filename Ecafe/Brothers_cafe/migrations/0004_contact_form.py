# Generated by Django 3.2.4 on 2022-08-28 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Brothers_cafe', '0003_auto_20220827_1412'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=15)),
                ('lname', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
