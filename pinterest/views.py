from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from pins.models import Pin


@login_required
def home(request):
    pins = Pin.objects.all()
    context = {'pins':pins[:49]}
    return render(request, 'home.html', context)


@login_required
def search(request):
    query = request.GET.get('q')
    pins = Pin.objects.filter(
        title__icontains=query,
        description__icontains=query).all()
    context = {'pins':pins[:49]}
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')

def business(request):
    return render(request, 'business.html')

def blog(request):
    return render(request, 'blog.html')



