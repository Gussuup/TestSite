from django.db import models

class Task(models.Model):                                       #Создание таблицы
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):                                          #магический метод, вывод поля title на экран вместо хеш кода
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'