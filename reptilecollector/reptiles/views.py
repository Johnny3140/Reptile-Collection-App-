from django.shortcuts import render, get_object_or_404
from .models import Reptile

def index(request):
    reptiles = Reptile.objects.all()
    return render(request, 'reptiles/index.html', {'reptiles': reptiles})

def about(request):
    return render(request, 'reptiles/about.html')

def reptile_detail(request, reptile_id):
    reptile = get_object_or_404(Reptile, pk=reptile_id)
    return render(request, 'reptiles/reptile_detail.html', {'reptile': reptile})

def reptile_index(request):
    reptiles = Reptile.objects.all()
    return render(request, 'reptiles/reptile_index.html', {'reptiles': reptiles})
