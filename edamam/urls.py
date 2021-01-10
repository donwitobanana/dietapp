from rest_framework import routers

from edamam.views import FoodViewSet

router = routers.SimpleRouter()
router.register(r'foods', FoodViewSet)

urlpatterns = router.urls
