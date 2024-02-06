from django.shortcuts import render
from .models import Reptile

def index(request):
    reptiles = Reptile.objects.all()
    return render(request, 'reptiles/index.html', {'reptiles': reptiles})

def about(request):
    return render(request, 'reptiles/about.html')
