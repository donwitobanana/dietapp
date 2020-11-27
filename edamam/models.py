from django.db import models


class Qualifier(models.Model):
    uri = models.CharField(max_length=100)
    label = models.CharField(max_length=20)


class Measure(models.Model):
    uri = models.CharField(max_length=70, unique=True)
    label = models.CharField(max_length=20)
    weight = models.FloatField(help_text='weight of the measure in grams')


class MeasureQualifier(models.Model):
    measure = models.ForeignKey(Measure, on_delete=models.CASCADE)
    qualifiers = models.ForeignKey(Qualifier, on_delete=models.CASCADE, null=True)
    weight = models.FloatField()


class Food(models.Model):
    edamam_id = models.CharField(max_length=50, unique=True)
    label = models.CharField(max_length=100)
    category = models.CharField(max_length=20)
    category_label = models.CharField(max_length=10)


class FoodMeasure(models.Model):
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE)
    measure_id = models.ForeignKey(Measure, on_delete=models.CASCADE)


class Nutrient(models.Model):
    nutrient_code = models.CharField(max_length=15)
    label = models.CharField(max_length=30)


class Unit(models.Model):
    name = models.CharField(max_length=10)


class FoodNutrient(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    nutrient = models.ForeignKey(Nutrient, on_delete=models.PROTECT)
    quantity = models.FloatField()
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT)
