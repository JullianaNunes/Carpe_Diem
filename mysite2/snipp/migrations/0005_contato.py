# Generated by Django 2.2.12 on 2020-06-02 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snipp', '0004_auto_20200601_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('assunto', models.CharField(blank=True, max_length=100, null=True)),
                ('mensagem', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]
