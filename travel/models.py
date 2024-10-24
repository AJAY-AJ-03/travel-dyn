from django.db import models

class Travels(models.Model):
    place = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    image = models.ImageField(upload_to='travel_images/')  # This will upload images to the 'travel_images' directory
    description = models.TextField()
    people = models.IntegerField()
    distance = models.FloatField()  # You can use FloatField to represent distance
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price field with 2 decimal places

    def __str__(self):
        return self.place  # This will display the travel place name in the admin
