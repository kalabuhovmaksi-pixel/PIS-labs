from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'index.html', {})


def hello(request):
    return HttpResponse("Привет, Мир!", content_type="text/plain; charset=utf-8")
