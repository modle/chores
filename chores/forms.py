from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm

from .models import Chores, Category, Rewards


class ChoresForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ChoresForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'placeholder': 'Title'})
        self.fields['title'].widget.attrs.update({'id': 'title'})
        self.fields['title'].widget.attrs.update({'class': 'form__field'})
        self.fields['category'].widget.attrs.update({'id': 'category'})
        self.fields['category'].widget.attrs.update({'class': 'form__field'})
        self.fields['primary_assignee'].widget.attrs.update({'id': 'primary_assignee'})
        self.fields['primary_assignee'].widget.attrs.update({'class': 'form__field'})
        self.fields['secondary_assignee'].widget.attrs.update({'id': 'secondary_assignee'})
        self.fields['secondary_assignee'].widget.attrs.update({'class': 'form__field'})
        self.fields['frequency_in_days'].widget.attrs.update({'id': 'frequency_in_days'})
        self.fields['frequency_in_days'].widget.attrs.update({'class': 'form__field'})
        self.fields['priority'].widget.attrs.update({'id': 'priority'})
        self.fields['priority'].widget.attrs.update({'class': 'form__field'})
        self.fields['time_in_minutes'].widget.attrs.update({'id': 'time_in_minutes'})
        self.fields['time_in_minutes'].widget.attrs.update({'class': 'form__field'})
        self.fields['effort'].widget.attrs.update({'id': 'effort'})
        self.fields['effort'].widget.attrs.update({'class': 'form__field'})

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
            'primary_assignee': 'Owner',
            'secondary_assignee': 'Backup',
            'frequency_in_days': 'Frequency (in days)',
            'priority': 'Priority',
            'time': 'Time (in minutes)',
            'effort': 'Level of Effort',
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


class MyAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(MyAuthenticationForm, self).__init__(*args, **kwargs)
        self.base_fields['username'].widget.attrs['placeholder'] = 'Username'
        self.base_fields['username'].widget.attrs['id'] = 'login__username'
        self.base_fields['username'].widget.attrs['class'] = 'form__input'
        self.base_fields['password'].widget.attrs['placeholder'] = 'Password'
        self.base_fields['password'].widget.attrs['id'] = 'login__password'
        self.base_fields['password'].widget.attrs['class'] = 'form__input'

    class Meta:
        fields = ('username', 'password', )
