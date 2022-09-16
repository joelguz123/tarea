from dataclasses import fields
from django import forms
from .models import Cursor

class CursorForm(forms.ModelForm):
    class Meta:
        model = Cursor
        fields = '__all__'