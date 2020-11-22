from django.core.management.base import BaseCommand, CommandError
from edamam.api_client import EdamamApiClient

class Command(BaseCommand):

    def handle(self, *args, **options):
        response = EdamamApiClient().get_food('brown rice')
        print(response)