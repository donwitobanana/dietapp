class FoodMapper:

    @staticmethod
    def map_hints(food_dto):
        hints = food_dto['hints']
        for hint in hints:
            food_info = hint['food']
            mapped_hint = {
                'food_id': food_info['foodId'],
                'label': food_info['label'],
                'category': food_info['category'],
                'category_label': food_info['categoryLabel']
            }
            measures = hint['measures']
            yield mapped_hint, measures