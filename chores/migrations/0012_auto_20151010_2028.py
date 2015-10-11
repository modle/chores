# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chores', '0011_auto_20151003_2218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('current_score', models.IntegerField(default=0)),
                ('total_score', models.IntegerField(default=0)),
                ('last_redeemed', models.DateTimeField(null=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('user',),
            },
        ),
        migrations.RemoveField(
            model_name='history',
            name='redeemed',
        ),
    ]
