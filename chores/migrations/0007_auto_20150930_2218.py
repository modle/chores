# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import chores.models


class Migration(migrations.Migration):

    dependencies = [
        ('chores', '0006_chores_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chores',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='chores.Category', null=True),
        ),
        migrations.AlterField(
            model_name='chores',
            name='last_completed_date',
            field=models.DateTimeField(default=chores.models.two_hundred_days_ago),
        ),
    ]
