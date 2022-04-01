from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/Главная.html')

def categories(request):
    return render(request, 'main/Категории.html')

def create(request):
    return render(request, 'main/Сделать-заказ.html')
