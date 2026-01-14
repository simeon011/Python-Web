from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from destination.models import Destination
from review.models import Review


DEFAULT_REVIEW = 5

def recent_reviews(request: HttpRequest) -> HttpResponse:
    review_count = request.GET.get(key='review_count', default=DEFAULT_REVIEW)
    reviews = Review.objects.order_by('-created_at')[:int(review_count)]

    context = {
        'recent_reviews': reviews,
        'page_title': 'Recent Review'
    }

    return render(request, 'review/list.html', context)


def review_detail(request, pk: int):
    review = get_object_or_404(Review, pk=pk)

    context = {
        'review': review,
        'page_title': f'{review.author} review',
    }

    return render(request, 'review/detail.html', context)