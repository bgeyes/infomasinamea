from .api import MakeViewSet, ModelViewSet, ReviewViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'make', MakeViewSet)
router.register(r'model', ModelViewSet)
router.register(r'review', ReviewViewSet)

urlpatterns = router.urls
