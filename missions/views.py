from django.shortcuts import render, redirect
from .models import Photos, Testimony, Message
from .forms import MessageForm, TestimonyForm


# Create your views here.

def index(request):
    images = Photos.objects.all()
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'images': images,
        'form': form
    }
    return render(request, 'missions/home.html', context)


def testimony(request):
    form = TestimonyForm()
    if request.method == 'POST':
        form = TestimonyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimony')
    context = {
        'form': form
    }
    return render(request, 'missions/testimony.html', context)

def testimony(request):
    form = TestimonyForm()
    if request.method == 'POST':
        form = TestimonyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimony')
    context = {
        'form': form
    }
    return render(request, 'missions/testimony.html', context)

