# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0001_initial'),
        ('hostinfo', '0006_auto_20171001_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostinfo',
            name='owner_group',
            field=models.ForeignKey(default=1, to='userinfo.Group'),
        ),
    ]
