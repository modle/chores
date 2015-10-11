# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('chores', '0013_auto_20151011_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rewards',
            name='last_redeemed_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
