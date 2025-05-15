from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.shortcuts import redirect
from django.http import HttpRequest

import json

from .models import Campus, Game, Movie

class IndexView(TemplateView):
    template_name = "pages/index.html"
    
class AboutView(TemplateView):
    template_name = "pages/about.html"

class CampusCreate(CreateView):
    template_name = "pages/form.html"
    model = Campus
    fields = [ "name" ]
    success_url = reverse_lazy("index")
    extra_context = { "titulo": "Cadastro de Campus" }

def create_game(request: HttpRequest):
    game = Game.objects.create()
    
    if (request.user.is_authenticated):
        game.user = game.user

    # Get random movie from database
    game.movie = Movie.objects.order_by("?").first()

    # Get 3 random movies as choices, plus the actual movie
    options = [movie.name for movie in Movie.objects.order_by("?")[:3]]
    options.append(game.movie.name)

    game.options = json.dumps(options)

    return redirect("play_game", uuid=game.uuid)
