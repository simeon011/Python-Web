from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from tasks.models import Task


# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    all_tasks = Task.objects.all()

    context = {
        'tasks': all_tasks,
    }
    return render(request, 'index.html', context)

def index2(request: HttpRequest) -> HttpResponse:
    all_tasks = Task.objects.all()

    template = [
        '<h1>All Tasks</h1>',
        *[f"<h3>{t.title} - {t.text}</h3>"for t in all_tasks]
    ]

    return HttpResponse('\n'.join(template))
