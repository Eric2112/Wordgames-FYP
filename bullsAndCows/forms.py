from django import forms
from bullsAndCows.models import LogMessage

class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message",)   # NOTE: the trailing comma is required


class GuessForm(forms.Form):
    your_guess = forms.CharField(label = 'Your guess', max_length =4)

    #def clean(self):
    #cleaned_data = super(GuessForm, self).clean()
    #guess = cleaned_data.get('guess')
    #if not guess:
     #       raise forms.ValidationError('You have to write something!')

#class GuessForm(forms.Form):
 #   guess = forms.CharField(label='guess', max_length=40)
