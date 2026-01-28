from django.shortcuts import render, get_object_or_404, redirect

from reviews.forms import CreateReviewForm, DeleteReviewForm
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

def create_review(request):
    form = CreateReviewForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("reviews:recent")

    context = {
        'form': form,
    }

    return render(request, 'reviews/create.html', context)

def update_review(request, pk):
    review = Review.objects.get(pk=pk)
    form = CreateReviewForm(request.POST or None, instance=review)
    if form.is_valid():
        form.save()
        return redirect("reviews:recent")

    context = {
        'form': form,
    }

    return render(request, 'reviews/edit.html', context)

def delete_review(request, pk):
    review = Review.objects.get(pk=pk)
    form = DeleteReviewForm(request.POST or None, instance=review)
    if form.is_valid():
        review.delete()
        return redirect("reviews:recent")

    context = {
        'form': form
    }
    return render(request, 'reviews/delete.html', context)