from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Todo(models.Model):
    text = models.TextField()
    slug = models.SlugField(max_length=100, null=True)
    test_field = models.TextField(default='')

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('todo:detail', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.text)
        super().save(*args, **kwargs) 
