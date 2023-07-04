from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

# Create your views here.
class BoardList(ListView):
    model = Board
    
class BoardDetail(DetailView):
    model = Board
