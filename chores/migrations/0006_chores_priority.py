# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chores', '0005_auto_20150928_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='chores',
            name='priority',
            field=models.IntegerField(default=1, choices=[(1, b'Hair is on fire'), (2, b'Mental stability requirement'), (3, b'Hide it under the rug')]),
        ),
    ]
