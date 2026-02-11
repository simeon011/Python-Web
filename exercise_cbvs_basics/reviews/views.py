from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from reviews.forms import reviewForm
from reviews.models import Review


class ReviewCreateView(CreateView):
    model = Review
    form_class = reviewForm
    success_url = reverse_lazy('common:home')
