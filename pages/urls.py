from django.urls import path, include
from .views import IndexView, AboutView, CampusCreate, create_game

urlpatterns = [
   path("", IndexView.as_view(), name="index"),
   path("about/", AboutView.as_view(), name="about"),
   path("campus/", CampusCreate.as_view(), name="campus"),
   path("accounts/", include("django.contrib.auth.urls")),

   path("play", create_game, name="create_game"),
   path("play/<str:uuid>", name="play_game"),
]
