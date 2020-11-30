from django.conf import settings
import requests

class EdamamApiClient:
    def __init__(self):
        self.application_id = settings.EDAMAM_API_APP_ID
        self.token = settings.EDAMAM_API_TOKEN
        self.base_url = settings.EDAMAM_API_BASE_URL

    def _generate_uri(self, uri_path):
        return f'{self.base_url}/{uri_path}'

    def _generate_auth_headers(self):
        return {'app_id': self.application_id, 'app_key': self.token}

    def get_food(self, lookup_value, by_upc=False):
        uri = self._generate_uri('parser')
        payload = self._generate_auth_headers()
        if by_upc:
            payload['upc'] = lookup_value
        else:
            payload['ingr'] = lookup_value
        response = requests.get(uri, params=payload)
        response.raise_for_status()
        return response.json()

    def get_nutrients(self, edamam_id, measure_uri, quantity=1):
        uri = self._generate_uri('nutrients')
        auth_headers = self._generate_auth_headers()
        payload = {
            "ingredients": [
                {
                "quantity": quantity,
                "measureURI": measure_uri,
                "foodId": edamam_id
                }
            ]
        }
        response = requests.post(uri, params=auth_headers, json=payload)
        response.raise_for_status()
        return response.json()
