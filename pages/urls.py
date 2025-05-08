from django.urls import path, include
from .views import IndexView, AboutView, CampusCreate

urlpatterns = [
   path("", IndexView.as_view(), name="index"),
   path("about/", AboutView.as_view(), name="about"),
   path("campus/", CampusCreate.as_view(), name="campus"),
   path("accounts/", include("django.contrib.auth.urls")),
]
