from rest_framework import serializers

from edamam.models import Food


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
