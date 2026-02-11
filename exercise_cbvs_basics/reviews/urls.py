from reviews import views
from django.urls import path

app_name = 'reviews'
urlpatterns = [
    path('create/', views.ReviewCreateView.as_view(), name='create'),
]