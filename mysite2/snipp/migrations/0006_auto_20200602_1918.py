# Generated by Django 2.2.12 on 2020-06-02 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snipp', '0005_modelemail_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelemail',
            name='numero',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
