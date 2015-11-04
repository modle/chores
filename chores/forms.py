from django import forms
from django.forms import ModelForm
from chores.choices import *

from .models import Chores, Category, Rewards


class ChoresForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ChoresForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'placeholder': 'Title'})
        self.fields['title'].widget.attrs.update({'id': 'title'})

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
