# Generated by Django 2.2.1 on 2019-06-09 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190609_0203'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
