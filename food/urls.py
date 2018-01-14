from django.urls import path
from food.views import FoodViewSet
from food.views import CategoryViewSet
from food.views import FilteredFoodViewSet
from rest_framework.routers import SimpleRouter
from food.routers import WithSlugReadOnlyRouter

urlpatterns = []

router = SimpleRouter()
router.register(r'instances', FoodViewSet, base_name='food')
router.register(r'categories', CategoryViewSet, base_name='category')
urlpatterns += router.urls

with_slug_router = WithSlugReadOnlyRouter()
with_slug_router.register(r'filtered', FilteredFoodViewSet, base_name='food-by-category')
urlpatterns += with_slug_router.urls
