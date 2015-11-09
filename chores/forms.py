from django import forms
from django.forms import ModelForm
from chores.choices import *

from .models import Chores, Category, Rewards


class ChoresForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ChoresForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'placeholder': 'Title'})
        self.fields['title'].widget.attrs.update({'id': 'title'})
        self.fields['category'].widget.attrs.update({'id': 'category'})
        self.fields['primary_assignee'].widget.attrs.update({'id': 'primary_assignee'})
        self.fields['secondary_assignee'].widget.attrs.update({'id': 'secondary_assignee'})
        self.fields['frequency_in_days'].widget.attrs.update({'id': 'frequency_in_days'})
        self.fields['priority'].widget.attrs.update({'id': 'priority'})
        self.fields['time_in_minutes'].widget.attrs.update({'id': 'time_in_minutes'})
        self.fields['effort'].widget.attrs.update({'id': 'effort'})

    class Meta:
        model = Chores
        fields = ('title',
                  'category',
                  'primary_assignee',
                  'secondary_assignee',
                  'frequency_in_days',
                  'priority',
                  'time_in_minutes',
                  'effort',)
        labels = {
            'title': '',
            'secondary_assignee': 'Backup',
            'primary_assignee': 'Owner',
            'frequency_in_days': 'Frequency (in days)',
            'priority': 'Priority',
            'time': 'Time (in minutes)',
            'effort': 'Level of Effort',
        }
        widgets = {
            'priority': forms.Select(),
        }
        choices = {
            'priority': PRIORITY_CHOICES,
        }
        initial = {
            'priority': '',
        }
        required = {
            'priority': True,
        }


class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'placeholder': 'Title'})

    class Meta:
        model = Category
        fields = ('title', )
        labels = {
            'title': 'title',
        }


class SearchForm(forms.Form):
    search_term = forms.CharField(label='', max_length=100)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['search_term'].widget.attrs.update({'placeholder': 'Filter'})


class RewardsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RewardsForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'placeholder': 'Title'})

    class Meta:
        model = Rewards
        fields = ('title', 'value', )
