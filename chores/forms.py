import itertools

from django import forms
from django.forms import ModelForm
from django.utils.text import slugify

from .models import Chores, Category


class ChoresForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ChoresForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'placeholder': 'Title'})
        self.fields['title'].widget.attrs.update({'id': 'title'})

    class Meta:
        model = Chores
        fields = ('title', 'category', 'primary_assignee', 'secondary_assignee', 'frequency_in_days', )
        labels = {
            'title': '',
            'secondary_assignee': 'Secondary Assignee',
            'primary_assignee': 'Primary Assignee',
            'frequency_in_days': 'Frequency (in days)',
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
    search_term = forms.CharField(label='Search', max_length=100)
