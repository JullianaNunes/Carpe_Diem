# Generated by Django 2.2.12 on 2020-06-03 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snipp', '0007_auto_20200602_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelemail',
            name='numero',
        ),
    ]