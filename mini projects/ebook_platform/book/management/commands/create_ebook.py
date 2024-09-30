from django.core.management.base import BaseCommand
from .models import Ebook, Poster

class Command(BaseCommand):
    help = 'Create a sample ebook and poster'

    def handle(self, *args, **kwargs):
        # Create an ebook instance
        ebook_instance = Ebook.objects.create(
            title="The Great Adventure",
            author="Jane Doe",
            description="A thrilling tale of adventure and discovery.",
            publication_date="2024-01-01",
            cover_image="covers/great_adventure_cover.jpg",
            file="ebooks/great_adventure.epub"
        )

        # Create a poster instance associated with the ebook
        poster_instance = Poster.objects.create(
            ebook=ebook_instance,
            poster_image="posters/great_adventure_poster.jpg",
            dimensions="24x36 inches"
        )

        self.stdout.write(self.style.SUCCESS('Ebook and poster created successfully.'))
