# Generated by Django 2.0 on 2020-02-20 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200213_1934'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': [('moderator', 'Can moderate content')]},
        ),
    ]
