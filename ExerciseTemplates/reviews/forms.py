
from django import forms
from reviews.models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

class CreateReviewForm(ReviewForm):
    ...

class UpdateReviewForm(ReviewForm):
    ...

class DeleteReviewForm(ReviewForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name in self.fields:
            self.fields[name].disabled = True



