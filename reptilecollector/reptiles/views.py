from django.shortcuts import render, get_object_or_404, redirect 
from .models import Reptile, Feeding
from .forms import ReptileForm, FeedingForm

def index(request):
    reptiles = Reptile.objects.all()
    return render(request, 'reptiles/index.html', {'reptiles': reptiles})

def about(request):
    return render(request, 'reptiles/about.html')

def reptile_detail(request, reptile_id):
    reptile = get_object_or_404(Reptile, pk=reptile_id)
    feedings = Feeding.objects.filter(reptile=reptile).order_by('-date')
    
    if request.method == 'POST':
        feeding_form = FeedingForm(request.POST)
        if feeding_form.is_valid():
            new_feeding = feeding_form.save(commit=False)
            new_feeding.reptile = reptile
            new_feeding.save()
            return redirect('reptile_detail', reptile_id=reptile_id)
    else:
        feeding_form = FeedingForm()

    return render(request, 'reptiles/reptile_detail.html', {'reptile': reptile, 'feedings': feedings, 'feeding_form': feeding_form})

def reptile_index(request):
    reptiles = Reptile.objects.all()
    return render(request, 'reptiles/reptile_index.html', {'reptiles': reptiles})

def add_reptile(request):
    if request.method == 'POST':
        form = ReptileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reptile_index')
    else:
        form = ReptileForm()

    return render(request, 'reptiles/add_reptile.html', {'form': form})

def edit_reptile(request, reptile_id):
    reptile = get_object_or_404(Reptile, pk=reptile_id)

    if request.method == 'POST':
        form = ReptileForm(request.POST, instance=reptile)
        if form.is_valid():
            form.save()
            return redirect('reptile_detail', reptile_id=reptile_id)
    else:
        form = ReptileForm(instance=reptile)

    return render(request, 'reptiles/edit_reptile.html', {'form': form, 'reptile': reptile})

def delete_reptile(request, reptile_id):
    reptile = get_object_or_404(Reptile, pk=reptile_id)
    
    if request.method == 'POST':
        reptile.delete()
        return redirect('reptile_index')

    return render(request, 'reptiles/delete_reptile.html', {'reptile': reptile})