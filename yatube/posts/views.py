from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    template = 'posts/index.html'
    context = {
        'title': 'Это главная страница проекта Yatube',
        'text': 'Текст',
    }
    return render(request, template, context)

def group(request):
    return HttpResponse(f'Страница группы')


def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title': title,
    }
    return render(request, template, context)