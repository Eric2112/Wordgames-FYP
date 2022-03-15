from django.urls import path
from bullsAndCows import views
from bullsAndCows.models import LogMessage

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
    path("chooseGame/", views.chooseGame, name="chooseGame"),
    path("check/", views.checkans, name = "check"),
    path("bullsCows/", views.bullsCows, name = "bullsCows"),
    path("bullsAndCowsAI", views.bullsAndCowsAI, name ="bullsAndCowsAI"),

  
]

