from edamam.api_client import EdamamApiClient
from edamam import models
from edamam.mappers import FoodMapper, MeasureMapper, NutrientMapper


class EdamamExtractor:
    def __init__(self):
        self.client = EdamamApiClient()


class FoodExtractor(EdamamExtractor):

    def load_extracted(self, lookup_value):
        food_obj, raw_measures = self._extract_food(lookup_value)
        for measure in raw_measures:
            measure_obj, weight, qualified = self._extract_measure(measure)
            if qualified:
                for qualifier_obj, weight in self._extracted_qualifiers(qualified):
                    self._create_food_measure(food_obj, measure_obj, weight, qualifier_obj)
            else:
                self._create_food_measure(food_obj, measure_obj, weight)
        return food_obj

    def _extract_food(self, lookup_value):
        food_dto = self.client.get_food(lookup_value)
        mapped_hints = FoodMapper.map_hints(food_dto)
        hint, raw_measures = next(mapped_hints)  # take first element only
        food_obj = self._create_food(hint)
        return food_obj, raw_measures

    def _extract_measure(self, measure_dto):
        mapped_measure = MeasureMapper.map_uri_label_object(measure_dto)
        measure_obj = self._create_measure(mapped_measure)

        weight = measure_dto['weight']

        qualified = measure_dto.get('qualified', [])

        return measure_obj, weight, qualified

    def _extracted_qualifiers(self, qualified):
        for qualified_dto in qualified:
            weight = qualified_dto['weight']
            for qualifier in qualified_dto['qualifiers']:
                qualifier_obj = self._create_qualifier(qualifier)
                yield qualifier_obj, weight

    def _create_food(self, food):
        edamam_id = food.pop('edamam_id')
        food_obj, _ = models.Food.objects.update_or_create(edamam_id=edamam_id, defaults=food)
        return food_obj

    def _create_measure(self, measure):
        measure_uri = measure.pop('uri')
        measure_obj, _ = models.Measure.objects.update_or_create(
            uri=measure_uri,
            defaults=measure
        )
        return measure_obj

    def _create_qualifier(self, qualifier):
        qualifier_uri = qualifier.pop('uri')
        qualifier_obj, _ = models.Qualifier.objects.update_or_create(
            uri=qualifier_uri,
            defaults=qualifier
        )
        return qualifier_obj

    def _create_food_measure(self, food, measure, weight, qualifier=None):
        food_measure_obj, _ = models.FoodMeasure.objects.update_or_create(
            food=food,
            measure=measure,
            qualifier=qualifier,
            defaults={'weight': weight}
        )
        return food_measure_obj


class NutrientExtractor(EdamamExtractor):

    def load_extracted(self, food_obj):
        for nutrient_obj, value, unit in self._extract_nutrients(food_obj.edamam_id):
            unit_obj, _ = models.Unit.objects.get_or_create(name=unit)
            self._create_food_nutrient(food_obj, nutrient_obj, unit_obj, value)

    def _extract_nutrients(self, edamam_id):
        measure_uri = models.Measure.objects.get(label='Gram').uri
        nutrients_dto = self.client.get_nutrients(edamam_id, measure_uri, quantity=100)
        for nutrient_info, value, unit in NutrientMapper.map_nutrients(nutrients_dto):
            nutrient_obj = self._create_nutrient(nutrient_info)
            yield nutrient_obj, value, unit

    def _create_nutrient(self, nutrient):
        nutrient_code = nutrient.pop('nutrient_code')
        nutrient_obj, _ = models.Nutrient.objects.update_or_create(nutrient_code=nutrient_code, defaults=nutrient)
        return nutrient_obj

    def _create_food_nutrient(self, food, nutrient, unit, value):
        food_nutrient_obj, _ = models.FoodNutrient.objects.update_or_create(
            food=food,
            nutrient=nutrient,
            unit=unit,
            defaults={'value': value}
        )
        return food_nutrient_obj
