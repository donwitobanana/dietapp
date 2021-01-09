from django.views.generic.list import ListView

from edamam.models import Food


class FoodListView(ListView):
    model = Food
    paginate_by = 100
