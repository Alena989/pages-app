from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
 
 
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView): 
    template_name = 'about.html'

class HamsterPageView(TemplateView):
    template_name = 'hamster.html'


class AnimalsPageView(TemplateView):
    template_name = 'animals.html'