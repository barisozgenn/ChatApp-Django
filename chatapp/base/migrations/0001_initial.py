# Generated by Django 4.1.4 on 2022-12-21 09:20

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MessageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('senderId', models.CharField(default='', max_length=200)),
                ('readers', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default='', max_length=200, null=True), default=list, size=None)),
                ('message', models.CharField(default='', max_length=200)),
                ('roomId', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MessageRoomModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default='', max_length=200, null=True), default=list, size=None)),
                ('roomName', models.CharField(default='', max_length=200)),
                ('lastMessageId', models.CharField(blank=True, default='', max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profileImageBase64', models.TextField(blank=True, null=True)),
                ('email', models.CharField(default='', max_length=200)),
                ('name', models.CharField(default='', max_length=200)),
                ('realmId', models.CharField(default='', max_length=256)),
            ],
        ),
    ]
