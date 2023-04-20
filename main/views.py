from django.shortcuts import render
from .models import Task

def index(request):
    tasks = Task.objects.all()                                                                                          #помещение в переменную всех объектов из модели Task

    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})                                     #Объединяет заданный шаблон с заданным контекстным словарем и возвращает
                                                                                                                        #объект HttpResponse с этим визуализированным кодом

def about(request):
    return render(request, 'main/about.html')

