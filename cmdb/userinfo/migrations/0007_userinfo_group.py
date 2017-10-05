# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0006_userinfo_is_actived'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='group',
            field=models.ManyToManyField(default=1, to='userinfo.Group'),
        ),
    ]
