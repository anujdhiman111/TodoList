# Generated by Django 4.2 on 2024-02-17 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='desc',
        ),
    ]