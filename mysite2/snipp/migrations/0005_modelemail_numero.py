# Generated by Django 2.2.12 on 2020-06-02 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snipp', '0004_auto_20200601_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelemail',
            name='numero',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
