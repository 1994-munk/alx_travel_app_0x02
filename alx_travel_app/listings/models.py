from django.db import models
from django.utils import timezone


# Listing model to represent a property or travel listing
class Listing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


# Booking model for reservations
class Booking(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bookings")
    guest_name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Booking for {self.listing.title} by {self.guest_name}"


# Review model for user feedback
class Review(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="reviews")
    reviewer_name = models.CharField(max_length=255)
    rating = models.IntegerField()  # scale 1–5
    comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Review {self.rating}/5 for {self.listing.title} by {self.reviewer_name}"
