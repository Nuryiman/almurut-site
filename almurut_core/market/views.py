from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'


class FavoritesView(TemplateView):
    template_name = 'favorites.html'

