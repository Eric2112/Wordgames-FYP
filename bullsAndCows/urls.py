from django.urls import path
from bullsAndCows import views

from django.views.generic import TemplateView

urlpatterns = [
    path("", views.startpage, name ="home"),
    path("startpage/", views.startpage, name = "startpage"),
    path("guess/", views.guess, name="guess"),
    path("correct/", views.correct, name="correct"),
    path("correctMixed/", views.correctMixed, name="correctMixed"),
    path("mixed/", views.mixed, name="mixed"),
    path("computerGuess", views.computerGuess, name ="computerGuess"),
    path("rules/", views.rules, name ="rules"),
    path("hangman/", views.hangman, name="hangman"),
    path("hang/", views.hang, name="hang"),
    path("hangmanWin/", views.hangmanWin, name="hangmanWin"),
    path("hangmanLose/", views.hangmanLose, name="hangmanLose"),
    path("chooseGame/", views.chooseGame, name="chooseGame"),
    path("checkans/", views.checkans, name = "checkans"),
    path("bullsCows/", views.bullsCows, name = "bullsCows"),
    path("bullsAndCowsAI", views.bullsAndCowsAI, name ="bullsAndCowsAI"),

  
]

