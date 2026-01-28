from django.urls import path, include

from books.views import landing_page, books_list, details, book_create, edit_book, delete_book

app_name = 'books'

urlpatterns = [
    path('', landing_page, name='home'),
    path('books/', include([
        path('', books_list, name='list'),
        path('create/', book_create, name='create'),
        path('<int:pk>/', include([
            path('edit/', edit_book, name='edit'),
            path('delete/', delete_book, name='delete'),
        ])),
        path('<slug:slug>/', details, name='details'),

    ]))
]