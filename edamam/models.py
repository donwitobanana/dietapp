from django.db import models
from enum import Enum


class Qualifier(models.Model):
    uri = models.CharField(max_length=100)
    label = models.CharField(max_length=20)


class Measure(models.Model):
    uri = models.CharField(max_length=70, unique=True)
    label = models.CharField(max_length=20)
    weight = models.FloatField(help_text='weight of the measure in grams')


class MeasureQualifier(models.Model):
    measure = models.ForeignKey(Measure, on_delete=models.CASCADE)
    qualifiers = models.ForeignKey(Qualifier, on_delete=models.CASCADE)
    weight = models.FloatField()


class Food(models.Model):
    edamam_id = models.CharField(max_length=50, unique=True)
    label = models.CharField(max_length=100)
    category = models.CharField(max_length=20)
    category_label = models.CharField(max_length=10)


class FoodMeasure(models.Model):
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE)
    measure_id = models.ForeignKey(Measure, on_delete=models.CASCADE)


class Nutrients(models.Model):
    food = models.OneToOneField(Food, on_delete=models.CASCADE)
    energy = models.FloatField()
    fat = models.FloatField()