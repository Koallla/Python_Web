from django import forms
from .models import Action

class DateTimeInput(forms.DateTimeInput):
    input_type = 'date'


class Select(forms.Select):
    input_type = 'select'


class ActionForm(forms.ModelForm):
    class Meta:
        model = Action
        fields = [
        'action_name',
        'category_name',
        'action_date',
        'action_count',
        ]

        widgets = {
        'action_date': DateTimeInput(attrs={'type': 'datetime-local'}),
        'action_name': Select(),
        'category_name': Select()
        }



class FilterForm(forms.Form):
    start = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    finish = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
