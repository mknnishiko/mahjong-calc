from django.shortcuts import render
from django.views.generic import ListView
from . . models import Player

class View(ListView):
    model = Player
    template_name = 'calc/index.html'
