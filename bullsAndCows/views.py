from unittest import removeHandler
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

import random
import os

class HomePage(TemplateView):
    template_name = 'bullsAndCows/startpage.html'

#not in use?
def guessReceived(request):
    return render(request, "bullsAndCows/guessReceived.html")

#not in use
def input(request):
    return render(request, "bullsAndCows/input.html")

words = [
    "hand",
    "sack",
    "zero",
    "name",
    "vial",
    "vile",
    "evil",
    "jean",
    "push",
    "chat",
    "face",
    "base",
    "mint",
    "fast",
    "tiny",
    "nope",
    "fork",
    "help",
    "stop",
    "poke",
    "lame",
    "pick",
    "bowl",
    "lent",
    "bent",
    "sent",
    "fire",
    "land",
    "sand",
    "rope",
    "soap",
    "trip",
    "slip",
    "pile",
    "pale",
    "spar",
    "soda",
    "cows",
    "crow",
]

#global variables for views
msg = ''
#i =0
count = 0

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
size = 4

def rword():
    global jword
    global word
    #global size
    word = random.choice(words)
    #size = len(word)

    #jum = random.sample(word, len(word))
    #jword = "".join(jum)


def checkans(request):
    global word 
    global msg 
    global jword
    global i

    user_answer = request.GET['answer']
    if user_answer == word:
        msg = "that was the correct word"
        guess(request)
        i = 0
        msg =" "
    else:
        msg = "you should try again"
        i += 1
    return render(request, "bullsAndCows/mixed.html", {'word': word, 'msg': msg, 'i': i })



def bullsCows(request):
    global word
    global msg
    count = 0
    bulls = 0
    cows = 0
    size = 4
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    # get a good guess
    msg =""
    guess = request.GET['answer'].strip()
    msg =""
    #count += 1
    if len(guess) == size and \
        all(char in letters for char in guess) \
        and len(set(guess)) == size:

        if guess == word:
                count += 1
                bulls = size
                cows = 0
                msg = "You guessed the correct word"    
        else:
            msg = ""
            msg = "You have not guessed the correct word"
            count += 1
            for i in range(size):
                if guess[i] == word[i]:
                    bulls += 1
                elif guess[i] in word:
                        cows += 1   
        return render(request, "bullsAndCows/guess.html", {'count': count, 'cows': cows, 'bulls': bulls, 'guess': guess, 'msg': msg })
    




def bullsAndCowsAI(request):

    return render(request, "bullsAndCows/computerGuess.html")


def mixed(request):
    return render(request, "bullsAndCows/mixed.html")


def rules(request):
    return render(request, "bullsAndCows/rules.html")

def startpage(request):
    return render(request, "bullsAndCows/startpage.html")

#possibly not in use
def get_Guess(request):
     if request.method == 'POST':
        form = GuessForm(request.POST)
        
        if form.is_valid():
            # Do something with the form data like send an email.
            return HttpResponseRedirect('/thanks/')
     else:
        form = GuessForm()

     return render(request, "bullsAndCows/guess.html", {'form': form})




def guess(request):
    rword()
    #global jword
    global msg
    return render(request, "bullsAndCows/guess.html", {'word': word, 'msg': msg})


def computerGuess(request):
    rword()
    #global jword
    global msg
    return render(request, "bullsAndCows/computerGuess.html", {'word' : word, 'msg' : msg})  


def computerAnswer(request):
    global word 
    global msg 
    #global jword
    global i

    user_answer = request.GET['answer']
    if user_answer == word:
        msg = "that was the correct word"
        guess(request)
        i = 0
        msg = 0
    else:
        msg = "you should try again"
        i += 1
    return render(request, "bullsAndCows/computerGuess.html", {'word': word, 'msg': msg, 'i': i })  

 


