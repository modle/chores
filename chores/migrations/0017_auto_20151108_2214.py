# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chores', '0016_auto_20151102_2125'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chores',
            options={'ordering': ('title',)},
        ),
    ]
