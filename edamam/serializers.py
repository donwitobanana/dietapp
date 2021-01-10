from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from edamam.models import Food, FoodNutrient, Nutrient, Unit


class NutrientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutrient
        exclude = ['id']


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        exclude = ['id']


class FoodNutrientSerializer(serializers.ModelSerializer):
    nutrient = NutrientSerializer(read_only=True)
    unit = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = FoodNutrient
        exclude = ['id', 'food']


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        exclude = ['edamam_id']


class FoodDetailSerializer(serializers.ModelSerializer):
    food_nutrients = FoodNutrientSerializer(many=True, read_only=True)

    class Meta:
        model = Food
        fields = ['id', 'label', 'category', 'food_nutrients']
