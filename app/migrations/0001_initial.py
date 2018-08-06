# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-01 09:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('back', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_num', models.IntegerField(default=1)),
                ('is_select', models.BooleanField(default=True)),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='back.BackProductList')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserModel')),
            ],
            options={
                'db_table': 'sx_carts',
            },
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_date', models.DateTimeField(auto_now=True)),
                ('o_pay', models.BooleanField(default=False)),
                ('o_total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('o_address', models.CharField(max_length=150)),
                ('o_peisong', models.CharField(max_length=50)),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='back.BackProductList')),
                ('o_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserModel')),
            ],
            options={
                'db_table': 'sx_orders',
            },
        ),
    ]