# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='unlockedkey',
            name='ts',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2014, 11, 23, 19, 39, 59, 929523, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
