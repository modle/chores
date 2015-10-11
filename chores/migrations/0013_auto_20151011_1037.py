# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chores', '0012_auto_20151010_2028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rewards',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, db_index=True)),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('value', models.IntegerField()),
                ('last_redeemed_date', models.DateTimeField(null=True)),
                ('last_redeemed_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.AlterModelOptions(
            name='history',
            options={'ordering': ('-completed_date', '-id')},
        ),
        migrations.RenameField(
            model_name='history',
            old_name='complete_date',
            new_name='completed_date',
        ),
        migrations.RenameField(
            model_name='score',
            old_name='last_redeemed',
            new_name='last_redeemed_date',
        ),
        migrations.AlterField(
            model_name='chores',
            name='effort',
            field=models.IntegerField(default=1, choices=[(1, b'Low'), (2, b'Medium'), (3, b'High')]),
        ),
    ]
