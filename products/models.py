from django.db import models


class Product(models.Model):
    title = models.TextField()
    image= models.ImageField(upload_to='images/')
    image2= models.ImageField(upload_to='images/')


    def __str__(self):
        return self.title