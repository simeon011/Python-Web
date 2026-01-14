from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from destination.models import Destination


# Create your views here.


def index(request: HttpRequest):
    return HttpResponse("welcome to our travel application")


def destination_list(request):
    destination = Destination.objects.all()

    context = {
        'destinations': destination,
        'page_title': 'Destination List'
    }

    return render(request, 'destinations/list.html', context)

def destination_detail(request, slug: str):
    destination = get_object_or_404(Destination, slug=slug)

    context = {
        'destination': destination,
        'page_title': f"{destination.name} Details",
    }

    return render(request, 'destinations/detail.html', context)

def redirect_home(request):
    return redirect('destination:list')