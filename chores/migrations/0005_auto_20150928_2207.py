# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import chores.models


class Migration(migrations.Migration):

    dependencies = [
        ('chores', '0004_auto_20150927_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chores',
            name='last_completed_by',
            field=models.ForeignKey(related_name='last_completed_by', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='chores',
            name='last_completed_date',
            field=models.DateTimeField(default=chores.models.one_hundred_days_ago),
        ),
    ]
