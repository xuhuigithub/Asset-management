# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostinfo', '0007_hostinfo_owner_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostinfo',
            name='owner_group',
            field=models.ForeignKey(to='userinfo.Group'),
        ),
    ]
