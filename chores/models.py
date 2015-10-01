from django.db import models
from django.db.models import permalink
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.contrib.auth.models import User

from chores.choices import *


def last_year():
    return timezone.now() - timezone.timedelta(days=365)

def two_hundred_days_ago():
    return timezone.now() - timezone.timedelta(days=200)


class History(models.Model):
    chore = models.ForeignKey('chores.Chores')
    complete_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        ordering = ('-complete_date', '-id')

    def __unicode__(self):
        return '{}'.format(self.chore)


class Chores(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey('chores.Category')
    primary_assignee = models.ForeignKey(User, related_name='primary_assignee')
    secondary_assignee = models.ForeignKey(User, null=True, blank=True, related_name='secondary_assignee')
    frequency_in_days = models.IntegerField(default=0)
    last_completed_date = models.DateTimeField(default=two_hundred_days_ago)
    last_completed_by = models.ForeignKey(User, related_name='last_completed_by', null=True, blank=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=1)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        super(Chores, self).save()

    def __unicode__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ('-id', )

    @permalink
    def get_absolute_url(self):
        return 'view_chore', None, {'slug': self.slug}


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        super(Category, self).save()

    def __unicode__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ('title', )

    @permalink
    def get_absolute_url(self):
        return 'view_category', None, {'slug': self.slug}
