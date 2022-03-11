from django.urls import path
from bullsAndCows import views
from bullsAndCows.models import LogMessage

from django.views.generic import TemplateView


urlpatterns = [
    path("", views.startpage, name ="home"),
    path("startpage/", views.startpage, name = "startpage"),
    path("guess/", views.guess, name="guess"),
    path("mixed/", views.mixed, name="mixed"),
    path("computerGuess", views.computerGuess, name ="computerGuess"),
    path("rules/", views.rules, name ="rules"),
    path("check/", views.checkans, name = "check"),
    path("bullsCows/", views.bullsCows, name = "bullsCows"),
    path("bullsAndCowsAI", views.bullsAndCowsAI, name ="bullsAndCowsAI"),
  
]

