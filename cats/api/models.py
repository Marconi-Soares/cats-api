from django.db import models

# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    image = models.ImageField(upload_to='cats')

    def __str__(self):
        return self.name
