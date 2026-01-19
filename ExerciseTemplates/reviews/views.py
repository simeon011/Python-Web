from django.shortcuts import render, get_object_or_404

from reviews.models import Review


def recent_reviews_list(request):
    reviews = Review.objects.select_related('book')
    return render(request, 'reviews/list.html', {
        'reviews': reviews,
    })
    return render(request, 'reviews/list.html', context)

def review_detail(request, pk):

    review = get_object_or_404(Review.objects.select_related('book'), pk=pk)

    context = {
        'review': review,
        'page_title': f"{review.author}'s review {review.book.title}",
    }
    return render(request, 'reviews/details.html', context)