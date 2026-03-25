from django.urls import path

from todos import views

urlpatterns = [
    path('', views.TodoListCreateAPIView.as_view(), name='list'),
    path('<int:pk>/', views.TodoDetailAPIView.as_view(), name='detail'),
    path('categories/', views.CategoriesListApiView.as_view(), name='list_category'),
]