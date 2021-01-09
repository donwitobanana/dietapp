from django.urls import path

from edamam.views import FoodListView

urlpatterns = [
    path('foods/', FoodListView.as_view(), name='food-list')
]