# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-29 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostinfo',
            name='ip_addr',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='hostinfo',
            name='ipmi_addr',
            field=models.CharField(max_length=20),
        ),
    ]
