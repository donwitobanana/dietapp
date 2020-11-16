from django.db import models

class TestModel(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
