from django import forms

from reviews.models import Review


class reviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ["created_at"]
