from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')

def categories(request):
    return render(request, 'main/categories.html')

def create(request):
    return render(request, 'main/create.html')

def new(request):
    return render(request, 'main/new.html')