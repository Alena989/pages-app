# pages/urls.py
from django.urls import path
 
from .views import HomePageView, AboutPageView, HamsterPageView, AnimalsPageView
 
urlpatterns = [
    path('animals/', AnimalsPageView.as_view(), name = 'animals'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('angry_hamster/', HamsterPageView.as_view(), name = 'hamster'),

]