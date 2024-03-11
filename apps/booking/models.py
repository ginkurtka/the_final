from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    description = models.TextField(max_length=1500)
    photos = models.ImageField(upload_to='hotel_photos/')
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
