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
