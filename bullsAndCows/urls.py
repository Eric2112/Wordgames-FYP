from django.urls import path
from bullsAndCows import views
from bullsAndCows.models import LogMessage

from django.views.generic import TemplateView

#home_list_view = views.HomeListView.as_view(
 #   queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
  #  context_object_name="message_list",
   # template_name="bullsAndCows/home.html",
#)

urlpatterns = [
    #path("", home_list_view, name="home"),
    path("", views.guess, name ="home"),
    path("input/", views.input, name="input"),
    path("guess/", views.guess, name="guess"),
    path("guess/<newform>", views.guess),
    path("log/", views.log_message, name="log"),
    path("guessReceived/", views.guessReceived, name="guessReceived"),
    path("guessReceived/guess", views.guess, name ="guessReceived"),
    path("computerGuess", views.computerGuess, name ="computerGuess"),
    path("rules/", views.rules, name ="rules"),
   # path("guessReceived/<newform>", views.guessReceived),
]

