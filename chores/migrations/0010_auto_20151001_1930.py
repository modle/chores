# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chores', '0009_auto_20150930_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chores',
            name='slug',
            field=models.SlugField(unique=True, max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='chores',
            unique_together=set([]),
        ),
    ]
