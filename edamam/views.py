from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from edamam.models import Food
from edamam.serializers import FoodSerializer, FoodDetailSerializer


class FoodViewSet(ViewSet):
    queryset = Food.objects.all()

    def list(self, request):
        serializer = FoodSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        food = get_object_or_404(self.queryset, pk=pk)
        serializer = FoodDetailSerializer(food)
        return Response(serializer.data)
