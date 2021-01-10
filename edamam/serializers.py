from rest_framework import serializers

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
    unit = UnitSerializer(read_only=True)

    class Meta:
        model = FoodNutrient
        exclude = ['food']


class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = '__all__'


class FoodDetailSerializer(serializers.ModelSerializer):

    food_nutrients = FoodNutrientSerializer(many=True, read_only=True)

    class Meta:
        model = Food
        fields = '__all__'