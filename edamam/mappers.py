class FoodMapper:

    @staticmethod
    def map_hints(food_dto):
        hints = food_dto['hints']
        for hint in hints:
            food_info = hint['food']
            mapped_hint = {
                'edamam_id': food_info['foodId'],
                'label': food_info['label'],
                'category': food_info['category'],
                'category_label': food_info['categoryLabel']
            }
            raw_measures = hint['measures']
            yield mapped_hint, raw_measures


class MeasureMapper:

    @staticmethod
    def map_uri_label_object(object_dto):
        return {
                'uri': object_dto['uri'],
                'label': object_dto['label']
            }


class NutrientMapper:

    @staticmethod
    def map_nutrients(nutrients_dto):
        nutrients = nutrients_dto['totalNutrients']
        for nutrient_code, nutrient_info in nutrients.items():
            nutrient = {'nutrient_code': nutrient_code, 'label': nutrient_info['label']}
            yield nutrient, nutrient_info['quantity'], nutrient_info['unit']