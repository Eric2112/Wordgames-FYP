from django.shortcuts import render
from django.shortcuts import redirect

from bullsAndCows.forms import LogMessageForm
from bullsAndCows.models import LogMessage
from django.views.generic import ListView
from bullsAndCows import methods

from django.views.generic.base import TemplateView

# Create your views here.
import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from bullsAndCows.forms import GuessForm
from django.urls import reverse

def get_Guess(request):
     if request.method == 'POST':
        form = GuessForm(request.POST)
        
        if form.is_valid():
            # Do something with the form data like send an email.
            return HttpResponseRedirect('bullsAndCows/guessReceived/')
     else:
        form = GuessForm()

     return render(request, 'bullsAndCows/guess.html', {'form': form})


#def get_guess(request):
 #   newform = GuessForm
  #  if request.method == 'POST':

   #     newform = GuessForm(request.POST)
        # check whether it's valid:
    #    if newform.is_valid():
            # process the data in form.cleaned_data as required
            
     #      print(newform.cleaned_data)
      #     Guess.objects.create(**newform.cleaned_data)
       # else: 
        #    print(newform.errors)
    #context ={
     #   "form" : newform
    #} 
  #  return render(request, 'bullsAndCows/guess.html', context)
   


#class HomeListView(ListView):
    #"""Renders the home page, with a list of all messages."""
    #model = LogMessage


    #def get_context_data(self, **kwargs):
     #   context = super(HomeListView, self).get_context_data(**kwargs)
      #  return context

class HomePage(TemplateView):
    template_name = 'bullsAndCows/guess.html'


#def guessReceived(request):
    #is_private = request.POST.get('is_private', False)
 #   guessReceived = request.POST['newform']
  #  return render(request, 'guessReceived.html',{'newform':guessReceived})
    #return HttpResponse('{}'.format(guess))

def guessReceived(request):
    return render(request, "bullsAndCows/guessReceived.html")


def input(request):
    return render(request, "bullsAndCows/input.html")

def guess(request):
    return render(request, "bullsAndCows/guess.html")


def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "bullsAndCows/log_message.html", {"form": form})  



def computerGuess(request):
    return render(request, "bullsAndCows/computerGuess.html")    

 


