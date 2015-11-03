# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chores', '0015_auto_20151011_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPreferences',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tile_color', models.CharField(default=b'8EEF8E', max_length=6)),
                ('chore_sorting', models.IntegerField(default=1, choices=[(1, b'Days Overdue'), (2, b'Priority'), (3, b'Effort'), (4, b'Last Completed'), (5, b'Completed By'), (6, b'Assigned To')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('user',),
            },
        ),
        migrations.AlterField(
            model_name='chores',
            name='priority',
            field=models.IntegerField(default=1, choices=[(1, b'Low'), (2, b'Medium'), (3, b'High')]),
        ),
    ]
