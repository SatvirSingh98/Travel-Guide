from django.db import models
from django.urls import reverse


# Create your models here.

class Destination(models.Model):
    name        = models.CharField(max_length=100)
    image       = models.ImageField(upload_to='images')
    title       = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price       = models.PositiveIntegerField()
    offer       = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('Travel:destination_description', kwargs={'name': self.name})

    def __str__(self):
        return self.name
    


class DestDescription(models.Model):
    place             = models.ForeignKey(Destination, related_name='place', on_delete=models.CASCADE)
    place_images      = models.ImageField(upload_to='images/place_images', blank=True)

    def __str__(self):
        return self.place.name
