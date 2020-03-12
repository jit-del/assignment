from django import forms
from .models import NoteData


class NoteForm(forms.ModelForm):
    class Meta:
        model = NoteData
        fields = "__all__"