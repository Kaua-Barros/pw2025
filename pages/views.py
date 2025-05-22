from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView
from django.shortcuts import redirect
from django.http import HttpRequest, HttpResponse

import json

from .models import Movie
from .forms import MovieForm

class IndexView(TemplateView):
    template_name = "pages/index.html"
    
class AboutView(TemplateView):
    template_name = "pages/about.html"

class MovieListView(ListView):
    model = Movie
    template_name = "pages/movie_list.html"  
    context_object_name = "movies"

class MovieCreateView(CreateView):
    model = Movie
    form_class = MovieForm
    template_name = "pages/movie_form.html"
    success_url = reverse_lazy("movie-list")
    extra_context = {"creating": True}

class MovieUpdateView(UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = "pages/movie_form.html"
    success_url = reverse_lazy("movie-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["creating"] = False
        context["movie_name"] = self.object.name
        return context

class MovieDeleteView(DeleteView):
    model = Movie
    template_name = "pages/movie_confirm_delete.html"
    success_url = reverse_lazy("movie-list")

# def create_game(request: HttpRequest):
#     # Get random movie from database
#     random_movie = Movie.objects.order_by("?").first()

#     if (random_movie is None):
#         return HttpResponse("No movies found", status=404)

#     game = Game.objects.create()
    
#     if (request.user.is_authenticated):
#         game.user = game.user

#     # Get 3 random movies as choices, plus the actual movie
#     options = [movie.name for movie in Movie.objects.order_by("?")[:3]]
#     options.append(game.movie.name)

#     game.options = json.dumps(options)

#     return redirect("play_game", uuid=game.uuid)
