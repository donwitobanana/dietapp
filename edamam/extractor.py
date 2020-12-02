from edamam.api_client import EdamamApiClient
from edamam import models
from edamam.mappers import FoodMapper


class FoodExtractor:
    target_model = models.Food
    def __init__(self):
        self.client = EdamamApiClient()

    def add_food(self, lookup_value):
        food_dto = self.client.get_food(lookup_value)
        mapped_hints = FoodMapper.map_hints(food_dto)
        hint, measures = next(mapped_hints)
        return hint, measures
