from django import forms
from bullsAndCows.models import LogMessage
from bullsAndCows.models import Guess

class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message",)   # NOTE: the trailing comma is required


class GuessForm(forms.ModelForm):
    class Meta:
        model = Guess
        fields =("guess",)



#class GuessForm(forms.Form):
 #   guess = forms.CharField(label='guess', max_length=40)
