# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0003_auto_20171005_1323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='name',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='username',
            field=models.CharField(default=b'xuhui', unique=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(unique=True, max_length=254),
        ),
    ]
