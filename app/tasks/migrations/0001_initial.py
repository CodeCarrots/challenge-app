# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UnlockedKey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('key', models.CharField(verbose_name='key', help_text='Unlocked key value.', max_length=128)),
                ('user', models.ForeignKey(related_name='unlocked_keys', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'unlocked key',
                'verbose_name_plural': 'unlocked keys',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='unlockedkey',
            unique_together=set([('user', 'key')]),
        ),
    ]
