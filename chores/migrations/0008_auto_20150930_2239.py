# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chores', '0007_auto_20150930_2218'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='chores',
            unique_together=set([('slug', 'category')]),
        ),
    ]
