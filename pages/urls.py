from django.urls import path, include
from .views import IndexView, AboutView, MovieListView, MovieCreateView, MovieUpdateView, MovieDeleteView

urlpatterns = [
   path("", IndexView.as_view(), name="index"),
   path("about/", AboutView.as_view(), name="about"),
   path("accounts/", include("django.contrib.auth.urls")),

   path("movies/", MovieListView.as_view(), name="movie-list"),
   path("movies/add/", MovieCreateView.as_view(), name="movie-create"),
   path("movies/<int:pk>/edit/", MovieUpdateView.as_view(), name="movie-update"),
   path("movies/<int:pk>/delete/", MovieDeleteView.as_view(), name="movie-delete"),

   # path("play", create_game, name="create_game"),
   # path("play/<str:uuid>", name="play_game"),
]
