import googlemaps

from django.db import models
from django.contrib.auth.models import User

from config.settings import GOOGLE_MAPS_API_KEY

google_maps_api_key = GOOGLE_MAPS_API_KEY

gmaps = googlemaps.Client(key=google_maps_api_key)


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        full_address = f"{self.name}, {self.address}"
        geocode_result = gmaps.geocode(full_address)
        if geocode_result:
            location = geocode_result[0]['geometry']['location']
            self.latitude = location['lat']
            self.longitude = location['lng']
        super().save(*args, **kwargs)

    

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='reviews')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()

    def __str__(self):
        return f"Review for {self.restaurant.name}"
    