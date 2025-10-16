from django.core.management.base import BaseCommand
from listings.models import Listing
import random


class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        sample_listings = [
            {"title": "Beachside Villa", "description": "Beautiful villa near the beach.", "price_per_night": 150.00, "location": "Mombasa"},
            {"title": "City Apartment", "description": "Modern apartment in the city center.", "price_per_night": 80.00, "location": "Nairobi"},
            {"title": "Safari Lodge", "description": "Experience wildlife like never before.", "price_per_night": 200.00, "location": "Maasai Mara"},
        ]

        for listing_data in sample_listings:
            Listing.objects.create(**listing_data)

        self.stdout.write(self.style.SUCCESS("Database seeded with sample listings!"))
