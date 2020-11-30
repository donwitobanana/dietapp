from django.core.management.base import BaseCommand
from edamam.api_client import EdamamApiClient  # pylint: disable=import-error

class Command(BaseCommand):

    def handle(self, *args, **options):
        response = EdamamApiClient().get_food('brown rice')
        print(response)
        