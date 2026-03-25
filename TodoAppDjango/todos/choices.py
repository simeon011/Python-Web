from django.db import models

class TodoStateChoices(models.TextChoices):
    DONE = 'Done', 'Done'
    NOT_DONE = 'Not Done', 'Not Done'