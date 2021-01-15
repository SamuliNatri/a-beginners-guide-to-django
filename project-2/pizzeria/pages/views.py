from django.views.generic import TemplateView
from django.views.generic.list import ListView
from pizzeria.pizzas.models import Pizza


class HomePageView(ListView):
    queryset = Pizza.objects.all().order_by('name')[:3]
    template_name = 'pages/home.html'
    context_object_name = 'pizzas'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'