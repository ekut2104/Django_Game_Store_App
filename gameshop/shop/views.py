from django.shortcuts import render
from django.http import HttpResponse
from .models import Game


# Create your views here.
def index(request):
    if request.method == "GET":
        return HttpResponse("Hello World!")


def get_games(request):
    if request.method == "GET":
        game = Game.objects.all()[0]
        return HttpResponse(str(game.title) + " $" + str(game.price))


def get_html(request):
    if request.method == "GET":
        return render(request, 'shop/index.html')
