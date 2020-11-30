from django.core.management.base import BaseCommand
from edamam.extractor import FoodExtractor  # pylint: disable=import-error

class Command(BaseCommand):

    def handle(self, *args, **options):
        output = FoodExtractor().add_food()
        print(output)