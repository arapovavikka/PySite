# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View


def homePageView(request):
    return HttpResponse('Hello, World!')

def index(request):
    # Отрисовка HTML-шаблона index.html с данными внутри 
    # переменной контекста context
    return render(
        request,
        'index.html'
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

class catalog(View):
    # Отрисовка HTML-шаблона index.html с данными внутри 
    # переменной контекста context
    #template_name = 'catalog.html'

    
        def get(self, request, *args, **kwargs):
      	    return render(request, 'catalog.html')

        def get_success_url(self):
	        return reverse('catalog')

class signin(View):

        def get(self, request, *args, **kwargs):
      	    return render(request, 'signin.html')

        def get_success_url(self):
	        return reverse('signin')



