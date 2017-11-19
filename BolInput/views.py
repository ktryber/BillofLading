from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
import datetime
from django.utils import timezone
from models import Load
from .forms import LoadForm

# Create your views here.

def load_list(request):
    loads = Load.objects.all().order_by('date_created')
    return render(request, 'load_list.html', {'loads':loads})

def load_detail(request, pk):
    load = get_object_or_404(Load, pk=pk)
    return render(request, 'load_detail.html', {'load': load})

def load_new(request):
    if request.method == "POST":
        form = LoadForm(request.POST)
        if form.is_valid():
            load = form.save(commit=False)
            load.date_created = timezone.now()
            load.save()
            return redirect('load_detail', pk=load.pk)
    else:
        form = LoadForm()
    return render(request, 'load_edit.html', {'form': form})

def load_edit(request, pk):
    load = get_object_or_404(Load, pk=pk)
    if request.method == "POST":
        form = LoadForm(request.POST, instance=load)
        if form.is_valid():
            load = form.save(commit=False)
            load.date_created = timezone.now()
            load.save()
            return redirect('load_detail', pk=load.pk)
    else:
        form = LoadForm(instance=load)
    return render(request, 'load_edit.html', {'form': form})