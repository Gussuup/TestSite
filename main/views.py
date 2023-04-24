from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all()                                                                                          #помещение в переменную всех объектов из модели Task

    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})                                     #Объединяет заданный шаблон с заданным контекстным словарем и возвращает
                                                                                                                        #объект HttpResponse с этим визуализированным кодом

def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Wrong form content'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)

