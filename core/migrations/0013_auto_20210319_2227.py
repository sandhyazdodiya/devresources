# Generated by Django 3.1.7 on 2021-03-19 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20210308_1308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='description',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='thumbnail',
        ),
    ]
