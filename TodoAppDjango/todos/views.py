from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveAPIView

from todos.filters import TodoFilter
from todos.models import Todo, Category
from todos.serializers import TodoSerializer, CategorySerializer, TodoNestedSerializer


class TodoListCreateAPIView(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_set_class = TodoFilter


class TodoDetailAPIView(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoNestedSerializer

class CategoriesListApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
