# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chores', '0010_auto_20151001_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='chores',
            name='effort',
            field=models.IntegerField(default=3, choices=[(1, b'High'), (2, b'Medium'), (3, b'Low')]),
        ),
        migrations.AddField(
            model_name='chores',
            name='time_in_minutes',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='history',
            name='redeemed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='history',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
