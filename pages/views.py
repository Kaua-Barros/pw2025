from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .models import Campus


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
