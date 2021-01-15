from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill


class Topping(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, 
                                decimal_places=2)
    toppings = models.ManyToManyField(Topping, 
                                      related_name='pizzas')
    image = models.ImageField(upload_to='images', 
                              blank=True)
    image_medium = ImageSpecField(source='image',
                                  processors=[ResizeToFill(350, 250)],
                                  format='JPEG',
                                  options={'quality': 60})
    image_detail = ImageSpecField(source='image',
                                  processors=[ResizeToFill(500, 100)],
                                  format='JPEG',
                                  options={'quality': 60})
    slug = models.SlugField(max_length=255, default='')
    published = models.BooleanField(null=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('pizzas:detail', args=[self.slug])
    
    def __str__(self):
        return self.name