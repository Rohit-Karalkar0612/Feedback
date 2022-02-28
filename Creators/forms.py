from django import forms
from .models import Event,Question

class Event_form(forms.ModelForm):
    class Meta:
        model=Event
        exclude = ('creator',)
class Question_form(forms.ModelForm):
    class Meta:
        model=Question
        exclude = ('event_related',)
