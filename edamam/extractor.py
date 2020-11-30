from random import randint

from edamam.api_client import EdamamApiClient
from edamam import models
from edamam.mappers import FoodMapper
from edamam.utils.upc_generator import UpcGenerator


class FoodExtractor:
    target_model = models.Food
    def __init__(self):
        self.client = EdamamApiClient()

    def add_food(self):
        upc_code = UpcGenerator.generate()
        food_dto = self.client.get_food(upc_code, by_upc=True)
        mapped_hints = FoodMapper.map_hints(food_dto)
        hint, measures = next(mapped_hints)
        return hint, measures
