from edamam.api_client import EdamamApiClient
from edamam import models
from edamam.mappers import FoodMapper, MeasureMapper


class FoodExtractor:
    def __init__(self):
        self.client = EdamamApiClient()

    def add_food(self, lookup_value):
        food_dto = self.client.get_food(lookup_value)
        mapped_hints = FoodMapper.map_hints(food_dto)
        hint, raw_measures = next(mapped_hints)
        edamam_id = hint.pop('edamam_id')
        food_obj, _ = models.Food.objects.update_or_create(edamam_id=edamam_id, defaults=hint)
        for measure_dto in raw_measures:
            mapped_measure = MeasureMapper.map_uri_label_object(measure_dto)
            measure_uri = mapped_measure.pop('uri')
            measure_obj, _ = models.Measure.objects.update_or_create(
                uri=measure_uri,
                defaults=mapped_measure
                )

            weight = measure_dto['weight']

            qualified = measure_dto.get('qualified')
            if qualified:
                for qualified_dto in qualified:
                    weight = qualified_dto['weight']
                    for qualifier in qualified_dto['qualifiers']:
                        qualifier_uri = qualifier.pop('uri')
                        qualifier_obj, _ = models.Qualifier.objects.update_or_create(
                            uri=qualifier_uri,
                            defaults=qualifier
                            )

                        models.FoodMeasure.objects.update_or_create(
                            food=food_obj,
                            measure=measure_obj,
                            qualifier=qualifier_obj,
                            defaults={'weight': weight}
                            )

            else:
                models.FoodMeasure.objects.update_or_create(
                        food=food_obj,
                        measure=measure_obj,
                        qualifier=None,
                        defaults={'weight': weight}
                        )
