from django import forms
from bullsAndCows.models import LogMessage

class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message",)   # NOTE: the trailing comma is required


class GuessForm(forms.Form):
    guess = forms.CharField(max_length=4)

#class GuessForm(forms.Form):
 #   guess = forms.CharField(label='guess', max_length=40)
