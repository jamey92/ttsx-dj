# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-01 09:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=64, unique=True)),
                ('recipients', models.CharField(default='', max_length=10)),
                ('uaddress', models.CharField(max_length=100)),
                ('postcode', models.CharField(max_length=6)),
                ('uphone', models.CharField(max_length=11)),
            ],
            options={
                'db_table': 'sx_users',
            },
        ),
        migrations.CreateModel(
            name='UserTicketModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket', models.CharField(max_length=256)),
                ('out_time', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserModel')),
            ],
            options={
                'db_table': 'sx_users_ticket',
            },
        ),
    ]
