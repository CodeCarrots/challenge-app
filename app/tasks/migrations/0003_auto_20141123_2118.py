# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_unlockedkey_ts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unlockedkey',
            name='ts',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
