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
import string

class HomePage(TemplateView):
    template_name = 'bullsAndCows/startpage.html'

#words for bulls and cows/ may add gutenberg dictionary or other api instead
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

#global variables for bulls and cows
msg = ''
i =0
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
    



#bulls and cows ai game views and code

    # this function picks letters and only moves 
    # on if a letter is not one in the guessed list
def new_letter(generateletter, alphabet):
    guessed_letter = 0
    guessed = []

    while generateletter:
            # Using random.choice to pick values
        guessed_letter = random.choice(alphabet)

        if guessed_letter not in guessed:
                for g in guessed:
                    if guessed_letter == g:
                            continue
                generateletter = False
        guessed.append(guessed_letter)

            # To prevent picking the same values again, remove them
        alphabet.remove(guessed_letter)
            #print('I guess '+str(guessed_letter))
        generateletter = False

        return guessed_letter


def bullsAndCowsAI(request):
    import string
    alphabet = []
    guessCount = 0

    playagain = True
    guessagain = True

    while playagain:

        user_word = request.GET['answer']

        
        actual_word = []
        computers_word = []

        for letter in user_word:
            actual_word.append(letter)
            computers_word.append('*')

        while guessagain:
            if computers_word != actual_word:
                alphabet = list(string.ascii_lowercase)
                alphabet.extend(list(string.ascii_uppercase))
                generateletter = True


                guessed_letter = new_letter(generateletter, alphabet)
                
                guessCount = guessCount+1

                # Used enumerate here to get position too
                # Additionally, used actual_word
                for i,letter in enumerate(actual_word):
                    if guessed_letter == letter:
                        # Insert at exactly the required position
                        computers_word[i] = guessed_letter

                    else:
                        continue

            elif computers_word == actual_word:
                #display_status
                string = ''.join([str(item) for item in actual_word])
               
                user_choice = request.POST.get('choice', False)
                if user_choice == 'Yes' or user_choice == 'yes':
                    guessagain = False
                    playagain = True

                else:
                    guessagain = False
                    playagain = False

    return render(request, "bullsAndCows/computerGuess.html", { 'guessCount': guessCount, 'actual_word':actual_word, 'user_word': user_word})




# basic views for loading webpages
def mixed(request):
    return render(request, "bullsAndCows/mixed.html")


def rules(request):
    return render(request, "bullsAndCows/rules.html")

def startpage(request):
    return render(request, "bullsAndCows/startpage.html")


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

 


