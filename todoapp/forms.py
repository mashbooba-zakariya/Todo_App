import datetime

from django import forms
from django.db import models

from todoapp.models import todo


class DateInput(forms.DateInput):
    input_type = 'date'

class todoForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = todo
        fields = ('title','date')

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')

        if date <= datetime.date.today():
            raise forms.ValidationError("this date is past !!!")
        return cleaned_data





