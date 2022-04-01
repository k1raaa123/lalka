from django.shortcuts import render


def index(request):
    return render(request, 'main/Glavnaya.html')


def categories(request):
    return render(request, 'main/Category.html')


def create(request):
    return render(request, 'main/Zakaz.html')
