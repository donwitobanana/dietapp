from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ReadOnlyModelViewSet

from edamam.extractor import FoodExtractor, NutrientExtractor
from edamam.models import Food
from edamam.serializers import FoodSerializer, FoodDetailSerializer


class FoodViewSet(ReadOnlyModelViewSet):
    serializers = {
        'list': FoodSerializer,
        'retrieve': FoodDetailSerializer
    }
    target_model = Food
    queryset = target_model.objects.all()

    def get_serializer_class(self):
        return self.serializers.get(self.action)

    def get_object(self):
        queryset = self.get_queryset()
        lookup_value = self.kwargs['pk']
        try:
            lookup_value = int(lookup_value)
            obj = get_object_or_404(queryset, pk=lookup_value)
        except ValueError:
            try:
                obj = queryset.get(label=lookup_value)
            except self.target_model.DoesNotExist:
                obj = self._add_food(lookup_value)
        return obj

    @classmethod
    def _add_food(cls, lookup_value):
        obj = FoodExtractor().load_extracted(lookup_value)
        NutrientExtractor().load_extracted(obj)
        return obj
