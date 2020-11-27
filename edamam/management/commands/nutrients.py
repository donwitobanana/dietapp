from django.core.management.base import BaseCommand
from edamam.api_client import EdamamApiClient

class Command(BaseCommand):

    def handle(self, *args, **options):
        response = EdamamApiClient().get_nutrients(
            edamam_id='food_aro09r9avsklizbsberuoaegj0uh', 
            measure_uri='http://www.edamam.com/ontologies/edamam.owl#Measure_kilogram'
            )
        print(response)
