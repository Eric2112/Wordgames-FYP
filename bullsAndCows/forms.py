from django import forms
from bullsAndCows.models import LogMessage

class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message",)   # NOTE: the trailing comma is required


class GuessForm(forms.Form):
    your_guess = forms.CharField(label = 'Your guess', max_length =4)


