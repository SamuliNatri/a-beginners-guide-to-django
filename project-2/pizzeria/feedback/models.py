from django.db import models


class Feedback(models.Model):
    text = models.TextField(null=True)
    screenshot = models.ImageField(upload_to='images',
                                   blank=True)
    
    def __str__(self):
        return self.text