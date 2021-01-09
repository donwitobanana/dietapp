from django.core.management.base import BaseCommand
from edamam.extractor import FoodExtractor, NutrientExtractor  # pylint: disable=import-error


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('lookup', help='lookup value', type=str)

    def handle(self, *args, **options):
        food_obj = FoodExtractor().load_extracted(options['lookup'])
        nutrient_output = NutrientExtractor().load_extracted(food_obj)
