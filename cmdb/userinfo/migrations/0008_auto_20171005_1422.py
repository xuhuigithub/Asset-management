# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0007_userinfo_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='group',
            field=models.ManyToManyField(to='userinfo.Group'),
        ),
    ]
