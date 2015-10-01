# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chores', '0008_auto_20150930_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chores',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
        migrations.AlterField(
            model_name='chores',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
