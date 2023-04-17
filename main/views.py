from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')              #Объединяет заданный шаблон с заданным контекстным словарем и возвращает
                                            #объект HttpResponse с этим визуализированным кодом

def about(request):
    return HttpResponse('<h4>About</h4>')
