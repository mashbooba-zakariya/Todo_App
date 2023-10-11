from django import forms

from todoapp.models import todo


class todoForm(forms.ModelForm):
    class Meta:
        model = todo
        fields = ('title',)
