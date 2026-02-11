from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from travelers.forms import TravelForm
from travelers.models import Traveler


class TravelerCreateView(CreateView):
    model = Traveler
    form_class = TravelForm
    success_url = reverse_lazy('common:home')

class TravelerUpdateView(UpdateView):
    model = Traveler
    form_class = TravelForm
    success_url = reverse_lazy('common:home')


class TravelerDeleteView(DeleteView):
    model = Traveler
    success_url = reverse_lazy('common:home')