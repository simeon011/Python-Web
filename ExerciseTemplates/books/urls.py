from django.urls import path, include

from books.views import landing_page, books_list, details


app_name = 'books'

urlpatterns = [
    path('', landing_page, name='home'),
    path('books/', include([
        path('', books_list, name='list'),
        path('<slug:slug>/', details, name='details')
    ]))
]