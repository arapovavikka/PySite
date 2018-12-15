# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .models import Post


def homePageView(request):
    return HttpResponse('Hello, World!')

def index(request):
    # Отрисовка HTML-шаблона index.html с данными внутри 
    # переменной контекста context
    posts = Post.objects.all()
    return render(
        request,
        'index.html',
        {'posts': posts}
    )

def cabinet(request):
    # Отрисовка HTML-шаблона index.html с данными внутри 
    # переменной контекста context
    return render(
        request,
        'cabinet.html'
    )

def project(request):
    # Отрисовка HTML-шаблона index.html с данными внутри 
    # переменной контекста context
    return render(
        request,
        'project.html'
    )

def projects(request):
    # Отрисовка HTML-шаблона index.html с данными внутри 
    # переменной контекста context
    return render(
        request,
        'projects.html'
    )

def catalog(request):
    # Отрисовка HTML-шаблона index.html с данными внутри 
    # переменной контекста context
    #template_name = 'catalog.html'
    return render(request, 'catalog.html')

def signin(request):
    return render(request, 'signin.html')

def about(request):
    return render(request, 'about.html')

def reg_org(request):
    return render(request, 'reg_org.html')

