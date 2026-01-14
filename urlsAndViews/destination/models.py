from django.db import models
from django.template.defaultfilters import slugify


class Destination(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField()
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.name and self.country:
            self.slug = slugify(f"{self.name} - {self.country}")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
