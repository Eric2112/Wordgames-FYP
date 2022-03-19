
from logging import raiseExceptions
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

#libraries we need for the views
import random
import os
import string
import time

#home page for website
class HomePage(TemplateView):
    template_name = 'bullsAndCows/startpage.html'

words = [
    "hand",
    "bags",
    "half",
    "soft",
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
    "kids",
]


#global variables for mixed word
msg = ''
i =0
error = ''

#global variables for bulls and cows
count = 0

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

#form random word for bulls and cows and mixed word game
def rword():
    global word
    word = random.choice(words)


def mixWord():
    global mixedWord
    global wordm
    global sizeM
    global i
    i = 0
    sizeM = 0
    wordm = random.choice(words)
    jum = random.sample(wordm, len(wordm))
    mixedWord = "".join(jum)
    sizeM = len(mixedWord)


def checkans(request):
    global wordm
    global msgMix 
    global mixedWord
    global i
    global sizeM

    userAnswer = request.GET['answer']
    i +=1
    
    if userAnswer == wordm and all(char in userAnswer for char in wordm):
                return render(request, "bullsAndCows/correctMixed.html", {'mixedWord': mixedWord, 'wordm': wordm, 'i':i, 'userAnswer':userAnswer})
    else:
                msgMix = "You have not guessed the correct word try again"
                print(mixedWord)
    
    return render(request, "bullsAndCows/mixed.html", {'mixedWord' : mixedWord,  'msgMix': msgMix, 'i': i, 'wordm':wordm })



def bullsCows(request):
    global word
    global msg
    global error
    global count
    bulls = 0
    cows = 0
    size = 4
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    # get a good guess
    msg =""
    guess = request.GET['answer'].strip()
    msg =""
    count += 1
    if len(guess) == size and \
        all(char in letters for char in guess) \
        and len(set(guess)) == size:
    
        if guess == word:
                finalCount = count
                count = 0
                bulls = size
                cows = 0
                return render(request, "bullsAndCows/correct.html", {'word':word, 
                'finalCount': finalCount, 'bulls':bulls})  
        else:
            msg = ""
            msg = "You have not guessed the correct word"
            for i in range(size):
                if guess[i] == word[i]:
                    bulls += 1
                elif guess[i] in word:
                        cows += 1 
        
        return render(request, "bullsAndCows/guess.html", {'count': count, 'cows': cows, 'bulls': bulls, 
        'guess': guess, 'msg': msg, 'word' :word })
    else:
        raise ValueError("This input is invalid. Please use 4 unique lowercase roman alphabet characters only")
        



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
        generateletter = False

        return guessed_letter


def bullsAndCowsAI(request):
    import string
    alphabet = []
    guessCount = 0
    cowsAI = 0
    bullsAI =0

    playagain = True
    guessagain = True

    while playagain:
        userWord = request.GET['answer']

        
        actualWord = []
        computersWord = []

        for letter in userWord:
            cowsAI += 1
            actualWord.append(letter)
            computersWord.append('*')

        while guessagain:
            if computersWord != actualWord:
                print(computersWord)
                print(bullsAI)
                print(cowsAI)
                alphabet = list(string.ascii_lowercase)
                #alphabet.extend(list(string.ascii_uppercase))
                generateletter = True


                guessed_letter = new_letter(generateletter, alphabet)
                
                guessCount = guessCount+1

                # Used enumerate here to get position too
                # Additionally, used actual_word
                for i,letter in enumerate(actualWord):
                    if guessed_letter == letter:
                        # Insert at exactly the required position
                        computersWord[i] = guessed_letter
                        bullsAI += 1
                        if bullsAI == len(actualWord):
                            computersWord = actualWord
                        cowsAI -= 1
                        if cowsAI == 0:
                            cowsAI = 0

                    else:
                        continue

            elif computersWord == actualWord:
                print(computersWord)
                print(bullsAI)
                print(cowsAI)
               
                user_choice = request.POST.get('choice', False)
                if user_choice == 'Yes' or user_choice == 'yes':
                    guessagain = False
                    playagain = True

                else:
                    guessagain = False
                    playagain = False

    return render(request, "bullsAndCows/computerGuess.html", { 'guessCount': guessCount, 'actualWord':actualWord, 'userWord': userWord, 'bullsAI':bullsAI, 'cowsAI': cowsAI})



#views relating to hangman

#load hangman template
def hangman(request):
    hangVariables()
    return render(request, "bullsAndCows/hangman.html")

#global variables for hangman 
def hangVariables():
    global hcount
    global hdisplay
    global hword
    global halready_guessed
    global hlength
    global hplay_game
    global totalHang
    global displayHang
    global showHang
    global showCorrect
    global wrongLetter
    #hwords_to_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage"
                   # ,"plants", "artifact"]
    hword = random.choice(words)
    showCorrect = hword
    hlength = len(hword)
    hcount = 0
    hdisplay = '_' * hlength
    halready_guessed = []
    hplay_game = ""
    totalHang = 0
    displayHang =""
    showHang = 0
    wrongLetter = []




def hang(request):
    global hcount
    global hdisplay
    global hword
    global halready_guessed
    global hplay_game
    global totalHang
    global showHang
    global showCorrect
    global wrongLetter
    hlimit = 5
  
    hguess = request.GET["answer"].strip()
    totalHang += 1
   
    if hguess in hword:
        halready_guessed.extend([hguess])
        hindex = hword.find(hguess)
        hword = hword[:hindex] + "_" + hword[hindex + 1:]
        hdisplay = hdisplay[:hindex] + hguess + hdisplay[hindex + 1:]
        print(hdisplay + "\n")
 
    #elif hguess in halready_guessed:
     #   print("Try another letter.\n")
 
    else:
        hcount += 1
        wrongLetter.extend(hguess)

 
        if hcount == 1:
            time.sleep(1)
           
 
        elif hcount == 2:
            time.sleep(1)
           
 
        elif hcount == 3:
           time.sleep(1)
           
 
        elif hcount == 4:
            time.sleep(1)
           
 
        elif hcount == 5:
            time.sleep(1)
           
            return render(request, "bullsAndCows/hangmanLose.html", {'hlimit': hlimit, 'hcount': hcount, 
        'hguess' : hguess, 'hword':hword, 'halready_guessed':halready_guessed, 
        'totalHang': totalHang, 'wrongLetter':wrongLetter, 'showCorrect': showCorrect})

 
    if hword == '_' * hlength:
        displayHang = "".join(halready_guessed)
        hlimit = 5
        hdisplay = '_' * hlength
        hplay_game = ""
      
        return render(request, "bullsAndCows/hangmanWin.html", {'hlimit': hlimit, 'hcount': hcount, 
        'hguess' : hguess, 'hword':hword, 'halready_guessed':halready_guessed, 'totalHang': totalHang, 'displayHang':displayHang, 'showCorrect' : showCorrect})
 
    elif hcount != hlimit:
        print(wrongLetter)

        return render(request, "bullsAndCows/hangman.html", {'hlimit': hlimit, 'hcount': hcount, 'hguess' : hguess, 
         'hword':hword, 'halready_guessed':halready_guessed, 'totalHang': totalHang, 'showCorrect':showCorrect, 'wrongLetter':wrongLetter})


def hangmanWin(request):

    return render(request, "bullsAndCows/hangmanWin.html")  

def hangmanLose(request):
    return render(request, "bullsAndCows/hangmanLose.html")  




# basic views for loading webpages
def chooseGame(request):
    return render(request, "bullsAndCows/chooseGame.html")

def mixed(request):
    mixWord()
    return render(request, "bullsAndCows/mixed.html", {'mixedWord' :mixedWord, 'wordm': wordm})


def rules(request):
    return render(request, "bullsAndCows/rules.html")

def startpage(request):
    return render(request, "bullsAndCows/startpage.html")



# views for human based 
def guess(request):
    rword()
    global msg
    return render(request, "bullsAndCows/guess.html", {'word': word, 'msg': msg})


def correct(request):
    return render(request, "bullsAndCows/correct.html")

def correctMixed(request):
    return render(request, "bullsAndCows/correctMixed.html")    


def computerGuess(request):
    rword()
    global msg
    return render(request, "bullsAndCows/computerGuess.html", {'word' : word, 'msg' : msg})  


 

 


