from rest_framework import routers
from .api import OfferViewSet

router = routers.DefaultRouter()
router.register('api/offers',OfferViewSet,'offers')
urlpatterns = router.urls