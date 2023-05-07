from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

from .models import Media
# Create your views here.
def peliculas (request):
    return render(request,'films/films.html')


    