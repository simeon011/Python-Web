from datetime import date


from django import forms


from books.models import Book


# class BookForm(forms.Form):
#     title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Harry Potter'}))
#     price = forms.DecimalField(max_digits=6, decimal_places=2, label="Price USD")
#     isbn = forms.CharField(max_length=12)
#     genre = forms.ChoiceField(choices=Book.GenreChoices.choices, widget=forms.RadioSelect)
#     publishing_date = forms.DateField(initial=date.today())
#     description = forms.CharField()
#     image_url = forms.URLField()
#     publisher = forms.CharField(max_length=100)


class BookForm(forms.ModelForm):
    class Meta:
        exclude = ['slug']
        model = Book

class CreateBookForm(BookForm):
    ...

class EditBookForm(BookForm):
    ...

class DeleteBookForm(BookForm):
    # class Meta(BookForm.Meta):
    #     widgets = {
    #         'title': forms.TextInput(
    #             attrs={'disabled': True}
    #         )
    #     }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name in self.fields:
            self.fields[name].disabled = True


class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100, label="Search")


