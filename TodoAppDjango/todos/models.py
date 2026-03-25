from django.contrib.auth import get_user_model
from django.db import models

from todos.choices import TodoStateChoices

UserModel = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=15)

class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='todos')
    state = models.BooleanField(choices=[
        (True, TodoStateChoices.DONE),
        (False, TodoStateChoices.NOT_DONE)
    ], default=False)
    assignees = models.ManyToManyField(UserModel, related_name='todos', blank=True)

    def __str__(self):
        return self.title
