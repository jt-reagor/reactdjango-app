# Generated by Django 4.0.6 on 2022-07-19 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rdapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='code',
            field=models.CharField(default='', max_length=50),
        ),
    ]
