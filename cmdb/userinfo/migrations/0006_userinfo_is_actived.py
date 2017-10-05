# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0005_auto_20171005_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='is_actived',
            field=models.BooleanField(default=True),
        ),
    ]
